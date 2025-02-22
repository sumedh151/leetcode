# https://www.geeksforgeeks.org/problems/preorder-traversal/1
#User function Template for python3



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
# recursive
class Solution:
#Function to return a list containing the preorder traversal of the tree.
    def preorder(self,root):
    # code here
        def traverse_preorder(node):
            if node is None:
                return []
            res = []
            res.append(node.data)
            res.extend(traverse_preorder(node.left))
            res.extend(traverse_preorder(node.right))
            return res
        
        return traverse_preorder(root)

# Given a binary tree, find its preorder traversal.

# Examples:

# Input:
#         1      
#       /          
#     4    
#   /    \   
# 4       2
# Output: [1, 4, 4, 2]

# Input:
#        6
#      /   \
#     3     2
#      \   / 
#       1 2
# Output: [6, 3, 1, 2, 2] 

# Input:
#          8
#        / \
#       3   10
#      / \    \
#     1   6   14
#        / \   /
#       4   7 13
# Output: [8, 3, 1, 6, 4, 7, 10, 14, 13]
