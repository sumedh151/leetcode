class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in nums_dict:
                return [i , nums_dict[target-nums[i]]]
            else:
                nums_dict[nums[i]] = i
        return []


import math
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

##########################################
# Positional Encoding
##########################################

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        """
        Implements the standard positional encoding as described in 
        'Attention is All You Need' (Vaswani et al.)
        """
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        
        # Create constant positional encoding matrix of shape (max_len, d_model)
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        # Compute the div term
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        # Apply sine to even indices and cosine to odd indices
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        # Add batch dimension
        pe = pe.unsqueeze(0)  # shape: (1, max_len, d_model)
        # Register as buffer (not a parameter, but saved with the model)
        self.register_buffer('pe', pe)
    
    def forward(self, x):
        """
        x: Tensor of shape (batch_size, seq_len, d_model)
        """
        x = x + self.pe[:, :x.size(1)]
        return self.dropout(x)

##########################################
# Self-Attention and Multi-Head Attention
##########################################

class SelfAttention(nn.Module):
    def __init__(self, d, dk, dv, mask):
        super(SelfAttention, self).__init__()
        self.query_layer = nn.Linear(d, dk)
        self.key_layer = nn.Linear(d, dk)
        self.value_layer = nn.Linear(d, dv)
        self.dk = dk
        self.mask = mask

    @staticmethod
    def mask_upper_tri_matrix(matrix):
        # Create an upper-triangular mask (with ones above the main diagonal)
        upper_triangle_mask = torch.triu(torch.ones_like(matrix, dtype=torch.bool), diagonal=1)
        return matrix.masked_fill(upper_triangle_mask, float('-inf'))

    def forward(self, x, enc_x=None):
        """
        x: Tensor of shape (batch_size, seq_len, d)
        enc_x: (optional) encoder output for cross-attention.
        """
        query = self.query_layer(x)  # (B, L, dk)
        if enc_x is not None:
            key   = self.key_layer(enc_x)
            value = self.value_layer(enc_x)
        else:
            key   = self.key_layer(x)
            value = self.value_layer(x)
        
        # Compute scaled dot-product attention scores
        scores = torch.bmm(query, key.transpose(1, 2)) / math.sqrt(self.dk)
        if self.mask:
            scores = SelfAttention.mask_upper_tri_matrix(scores)
        attn_weights = torch.softmax(scores, dim=-1)
        attn_output = torch.bmm(attn_weights, value)
        return attn_output

class MultiHeadAttention(nn.Module):
    def __init__(self, h, d, dk, dv, mask):
        super(MultiHeadAttention, self).__init__()
        self.h = h
        # We'll combine the output of each head and then project it back to d dimensions.
        self.out_linear = nn.Linear(h * dv, d)
        # Create h self-attention heads
        self.attention_heads = nn.ModuleList([SelfAttention(d, dk, dv, mask) for _ in range(h)])
        
    def forward(self, x, enc_x=None):
        head_outputs = []
        for head in self.attention_heads:
            head_output = head(x, enc_x)
            head_outputs.append(head_output)
        # Concatenate outputs along the feature dimension
        multihead_output = torch.cat(head_outputs, dim=-1)
        return self.out_linear(multihead_output)

##########################################
# Encoder and Decoder Blocks
##########################################

class EncoderBlock(nn.Module):
    def __init__(self, h, d, dk, dv, ffo_out):
        super(EncoderBlock, self).__init__()
        self.multihead_attn = MultiHeadAttention(h, d, dk, dv, mask=False)
        self.layer_norm1 = nn.LayerNorm(d)
        self.ff1 = nn.Linear(d, ffo_out)
        self.ff2 = nn.Linear(ffo_out, d)
        self.relu = nn.ReLU()
        self.layer_norm2 = nn.LayerNorm(d)
        
    def forward(self, x):
        # Multi-head self-attention with residual connection
        attn_out = self.multihead_attn(x)
        x = self.layer_norm1(x + attn_out)
        # Feed-forward network with residual connection
        ff_out = self.ff2(self.relu(self.ff1(x)))
        x = self.layer_norm2(x + ff_out)
        return x

class DecoderBlock(nn.Module):
    def __init__(self, h, d, dk, dv, ffo_out):
        super(DecoderBlock, self).__init__()
        self.d = d
        # First sub-layer: masked self-attention
        self.self_attn = MultiHeadAttention(h, d, dk, dv, mask=True)
        self.layer_norm1 = nn.LayerNorm(d)
        # Second sub-layer: cross-attention with encoder output
        self.cross_attn = MultiHeadAttention(h, d, dk, dv, mask=False)
        self.layer_norm2 = nn.LayerNorm(d)
        # Third sub-layer: feed-forward network
        self.ff1 = nn.Linear(d, ffo_out)
        self.ff2 = nn.Linear(ffo_out, d)
        self.relu = nn.ReLU()
        self.layer_norm3 = nn.LayerNorm(d)
        
    def forward(self, x, enc_x):
        # Masked self-attention + residual
        self_attn_out = self.self_attn(x)
        x = self.layer_norm1(x + self_attn_out)
        # Cross-attention + residual
        cross_attn_out = self.cross_attn(x, enc_x)
        x = self.layer_norm2(x + cross_attn_out)
        # Feed-forward network + residual
        ff_out = self.ff2(self.relu(self.ff1(x)))
        x = self.layer_norm3(x + ff_out)
        return x

##########################################
# Full Encoder and Decoder
##########################################

class Encoder(nn.Module):
    def __init__(self, num_layers, h, d, dk, dv, ffo_out):
        super(Encoder, self).__init__()
        self.layers = nn.ModuleList([EncoderBlock(h, d, dk, dv, ffo_out) for _ in range(num_layers)])
        
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

class Decoder(nn.Module):
    def __init__(self, num_layers, h, d, dk, dv, ffo_out):
        super(Decoder, self).__init__()
        self.layers = nn.ModuleList([DecoderBlock(h, d, dk, dv, ffo_out) for _ in range(num_layers)])
        
    def forward(self, x, enc_x):
        for layer in self.layers:
            x = layer(x, enc_x)
        return x

##########################################
# Transformer Model
##########################################

class Transformer(nn.Module):
    def __init__(self, tokenizer, num_layers=6, d=512, dk=64, dv=64, h=8, ffo_out=2048, dropout=0.1, max_len=5000):
        super(Transformer, self).__init__()
        self.tokenizer = tokenizer
        vocab_size = tokenizer.get_vocab_size()
        self.d = d
        self.inp_embedding = nn.Embedding(vocab_size, d)
        self.out_embedding = nn.Embedding(vocab_size, d)
        self.positional_encoding = PositionalEncoding(d_model=d, dropout=dropout, max_len=max_len)
        self.encoder = Encoder(num_layers, h, d, dk, dv, ffo_out)
        self.decoder = Decoder(num_layers, h, d, dk, dv, ffo_out)
        # Final projection layer (logits over vocabulary)
        self.projection = nn.Linear(d, vocab_size)
        self.softmax = nn.Softmax(dim=-1)
        
    def forward(self, input_tokens, output_tokens):
        # Encode the source sequence
        enc = self.inp_embedding(input_tokens)
        enc = self.positional_encoding(enc)
        enc = self.encoder(enc)
        # Decode using teacher forcing (shifted target sequence)
        dec = self.out_embedding(output_tokens)
        dec = self.positional_encoding(dec)
        dec = self.decoder(dec, enc)
        out = self.projection(dec)  # logits; do not apply softmax here because loss function expects raw logits
        out = self.softmax(out)
        return out

##########################################
# Pre-tokenized Dataset Loader (from previous step)
##########################################

class PreTokenizedDataset(Dataset):
    def __init__(self, file_path):
        # Assumes pre-tokenized data is saved as a list of (src_tokens, trg_tokens) tuples.
        self.data = torch.load(file_path)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        src_tokens, trg_tokens = self.data[idx]
        # Return tensors of type long
        return torch.tensor(src_tokens, dtype=torch.long), torch.tensor(trg_tokens, dtype=torch.long)

##########################################
# Training Loop
##########################################

# Device configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load your pre-tokenized data (make sure this file exists from your earlier preprocessing)
dataset = PreTokenizedDataset("pretokenized_data.pt")
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Load the tokenizer (assuming you used tokenizers library)
from tokenizers import Tokenizer
tokenizer = Tokenizer.from_file("bpe_tokenizer_combined.json")

# Instantiate the Transformer model
model = Transformer(tokenizer, num_layers=6, d=512, dk=64, dv=64, h=8, ffo_out=2048).to(device)

# Define optimizer and loss function.
# CrossEntropyLoss expects logits of shape (N, vocab_size) and target indices.
# We use ignore_index to avoid computing loss on PAD tokens.
pad_token_id = tokenizer.token_to_id("[PAD]")
criterion = nn.CrossEntropyLoss(ignore_index=pad_token_id)
optimizer = optim.Adam(model.parameters(), lr=1e-4)

num_epochs = 10

for epoch in range(num_epochs):
    model.train()
    total_loss = 0.0
    for src, trg in dataloader:
        # Move data to device
        src = src.to(device)  # Source sequence (e.g. English)
        trg = trg.to(device)  # Target sequence (e.g. Hindi), including start ([CLS]) & stop ([SEP]) tokens

        # For training, use teacher forcing.
        # Decoder input is target tokens up to the second-to-last token.
        # The expected output (target) is the target tokens shifted left (i.e. excluding the first token).
        decoder_input = trg[:, :-1]
        decoder_target = trg[:, 1:]
        
        optimizer.zero_grad()
        # Forward pass: obtain logits of shape (batch, seq_len, vocab_size)
        logits = model(src, decoder_input)
        # Reshape logits and targets to compute cross-entropy loss.
        # Flatten batch and sequence dimensions.
        logits = logits.reshape(-1, logits.size(-1))
        decoder_target = decoder_target.reshape(-1)
        loss = criterion(logits, decoder_target)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}")






import math
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

##########################################
# Positional Encoding
##########################################

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        """
        Implements the standard positional encoding as described in 
        'Attention is All You Need' (Vaswani et al.)
        """
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        
        # Create constant positional encoding matrix of shape (max_len, d_model)
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        # Compute the div term
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        # Apply sine to even indices and cosine to odd indices
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        # Add batch dimension
        pe = pe.unsqueeze(0)  # shape: (1, max_len, d_model)
        # Register as buffer (not a parameter, but saved with the model)
        self.register_buffer('pe', pe)
    
    def forward(self, x):
        """
        x: Tensor of shape (batch_size, seq_len, d_model)
        """
        x = x + self.pe[:, :x.size(1)]
        return self.dropout(x)

##########################################
# Self-Attention and Multi-Head Attention
##########################################

class SelfAttention(nn.Module):
    def __init__(self, d, dk, dv, mask):
        super(SelfAttention, self).__init__()
        self.query_layer = nn.Linear(d, dk)
        self.key_layer = nn.Linear(d, dk)
        self.value_layer = nn.Linear(d, dv)
        self.dk = dk
        self.mask = mask

    @staticmethod
    def mask_upper_tri_matrix(matrix):
        # Create an upper-triangular mask (with ones above the main diagonal)
        upper_triangle_mask = torch.triu(torch.ones_like(matrix, dtype=torch.bool), diagonal=1)
        return matrix.masked_fill(upper_triangle_mask, float('-inf'))

    def forward(self, x, enc_x=None):
        """
        x: Tensor of shape (batch_size, seq_len, d)
        enc_x: (optional) encoder output for cross-attention.
        """
        query = self.query_layer(x)  # (B, L, dk)
        if enc_x is not None:
            key   = self.key_layer(enc_x)
            value = self.value_layer(enc_x)
        else:
            key   = self.key_layer(x)
            value = self.value_layer(x)
        
        # Compute scaled dot-product attention scores
        scores = torch.bmm(query, key.transpose(1, 2)) / math.sqrt(self.dk)
        if self.mask:
            scores = SelfAttention.mask_upper_tri_matrix(scores)
        attn_weights = torch.softmax(scores, dim=-1)
        attn_output = torch.bmm(attn_weights, value)
        return attn_output

class MultiHeadAttention(nn.Module):
    def __init__(self, h, d, dk, dv, mask):
        super(MultiHeadAttention, self).__init__()
        self.h = h
        # We'll combine the output of each head and then project it back to d dimensions.
        self.out_linear = nn.Linear(h * dv, d)
        # Create h self-attention heads
        self.attention_heads = nn.ModuleList([SelfAttention(d, dk, dv, mask) for _ in range(h)])
        
    def forward(self, x, enc_x=None):
        head_outputs = []
        for head in self.attention_heads:
            head_output = head(x, enc_x)
            head_outputs.append(head_output)
        # Concatenate outputs along the feature dimension
        multihead_output = torch.cat(head_outputs, dim=-1)
        return self.out_linear(multihead_output)

##########################################
# Encoder and Decoder Blocks
##########################################

class EncoderBlock(nn.Module):
    def __init__(self, h, d, dk, dv, ffo_out):
        super(EncoderBlock, self).__init__()
        self.multihead_attn = MultiHeadAttention(h, d, dk, dv, mask=False)
        self.layer_norm1 = nn.LayerNorm(d)
        self.ff1 = nn.Linear(d, ffo_out)
        self.ff2 = nn.Linear(ffo_out, d)
        self.relu = nn.ReLU()
        self.layer_norm2 = nn.LayerNorm(d)
        
    def forward(self, x):
        # Multi-head self-attention with residual connection
        attn_out = self.multihead_attn(x)
        x = self.layer_norm1(x + attn_out)
        # Feed-forward network with residual connection
        ff_out = self.ff2(self.relu(self.ff1(x)))
        x = self.layer_norm2(x + ff_out)
        return x

class DecoderBlock(nn.Module):
    def __init__(self, h, d, dk, dv, ffo_out):
        super(DecoderBlock, self).__init__()
        self.d = d
        # First sub-layer: masked self-attention
        self.self_attn = MultiHeadAttention(h, d, dk, dv, mask=True)
        self.layer_norm1 = nn.LayerNorm(d)
        # Second sub-layer: cross-attention with encoder output
        self.cross_attn = MultiHeadAttention(h, d, dk, dv, mask=False)
        self.layer_norm2 = nn.LayerNorm(d)
        # Third sub-layer: feed-forward network
        self.ff1 = nn.Linear(d, ffo_out)
        self.ff2 = nn.Linear(ffo_out, d)
        self.relu = nn.ReLU()
        self.layer_norm3 = nn.LayerNorm(d)
        
    def forward(self, x, enc_x):
        # Masked self-attention + residual
        self_attn_out = self.self_attn(x)
        x = self.layer_norm1(x + self_attn_out)
        # Cross-attention + residual
        cross_attn_out = self.cross_attn(x, enc_x)
        x = self.layer_norm2(x + cross_attn_out)
        # Feed-forward network + residual
        ff_out = self.ff2(self.relu(self.ff1(x)))
        x = self.layer_norm3(x + ff_out)
        return x

##########################################
# Full Encoder and Decoder
##########################################

class Encoder(nn.Module):
    def __init__(self, num_layers, h, d, dk, dv, ffo_out):
        super(Encoder, self).__init__()
        self.layers = nn.ModuleList([EncoderBlock(h, d, dk, dv, ffo_out) for _ in range(num_layers)])
        
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

class Decoder(nn.Module):
    def __init__(self, num_layers, h, d, dk, dv, ffo_out):
        super(Decoder, self).__init__()
        self.layers = nn.ModuleList([DecoderBlock(h, d, dk, dv, ffo_out) for _ in range(num_layers)])
        
    def forward(self, x, enc_x):
        for layer in self.layers:
            x = layer(x, enc_x)
        return x

##########################################
# Transformer Model
##########################################

class Transformer(nn.Module):
    def __init__(self, tokenizer, num_layers=6, d=512, dk=64, dv=64, h=8, ffo_out=2048, dropout=0.1, max_len=5000):
        super(Transformer, self).__init__()
        self.tokenizer = tokenizer
        vocab_size = tokenizer.get_vocab_size()
        self.d = d
        self.inp_embedding = nn.Embedding(vocab_size, d)
        self.out_embedding = nn.Embedding(vocab_size, d)
        self.positional_encoding = PositionalEncoding(d_model=d, dropout=dropout, max_len=max_len)
        self.encoder = Encoder(num_layers, h, d, dk, dv, ffo_out)
        self.decoder = Decoder(num_layers, h, d, dk, dv, ffo_out)
        # Final projection layer (logits over vocabulary)
        self.projection = nn.Linear(d, vocab_size)
        self.softmax = nn.Softmax(dim=-1)
        
    def forward(self, input_tokens, output_tokens):
        # Encode the source sequence
        enc = self.inp_embedding(input_tokens)
        enc = self.positional_encoding(enc)
        enc = self.encoder(enc)
        # Decode using teacher forcing (shifted target sequence)
        dec = self.out_embedding(output_tokens)
        dec = self.positional_encoding(dec)
        dec = self.decoder(dec, enc)
        out = self.projection(dec)  # logits; do not apply softmax here because loss function expects raw logits
        out = self.softmax(out)
        return out

##########################################
# Pre-tokenized Dataset Loader (from previous step)
##########################################

class PreTokenizedDataset(Dataset):
    def __init__(self, file_path):
        # Assumes pre-tokenized data is saved as a list of (src_tokens, trg_tokens) tuples.
        self.data = torch.load(file_path)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        src_tokens, trg_tokens = self.data[idx]
        # Return tensors of type long
        return torch.tensor(src_tokens, dtype=torch.long), torch.tensor(trg_tokens, dtype=torch.long)

##########################################
# Training Loop
##########################################

# Device configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load your pre-tokenized data (make sure this file exists from your earlier preprocessing)
dataset = PreTokenizedDataset("pretokenized_data.pt")
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Load the tokenizer (assuming you used tokenizers library)
from tokenizers import Tokenizer
tokenizer = Tokenizer.from_file("bpe_tokenizer_combined.json")

# Instantiate the Transformer model
model = Transformer(tokenizer, num_layers=6, d=512, dk=64, dv=64, h=8, ffo_out=2048).to(device)

# Define optimizer and loss function.
# CrossEntropyLoss expects logits of shape (N, vocab_size) and target indices.
# We use ignore_index to avoid computing loss on PAD tokens.
pad_token_id = tokenizer.token_to_id("[PAD]")
criterion = nn.CrossEntropyLoss(ignore_index=pad_token_id)
optimizer = optim.Adam(model.parameters(), lr=1e-4)

num_epochs = 10

for epoch in range(num_epochs):
    model.train()
    total_loss = 0.0
    for src, trg in dataloader:
        # Move data to device
        src = src.to(device)  # Source sequence (e.g. English)
        trg = trg.to(device)  # Target sequence (e.g. Hindi), including start ([CLS]) & stop ([SEP]) tokens

        # For training, use teacher forcing.
        # Decoder input is target tokens up to the second-to-last token.
        # The expected output (target) is the target tokens shifted left (i.e. excluding the first token).
        decoder_input = trg[:, :-1]
        decoder_target = trg[:, 1:]
        
        optimizer.zero_grad()
        # Forward pass: obtain logits of shape (batch, seq_len, vocab_size)
        logits = model(src, decoder_input)
        # Reshape logits and targets to compute cross-entropy loss.
        # Flatten batch and sequence dimensions.
        logits = logits.reshape(-1, logits.size(-1))
        decoder_target = decoder_target.reshape(-1)
        loss = criterion(logits, decoder_target)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}")
