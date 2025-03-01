# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def contribution(self, node, memo_contri):
        if node is None:
            return float('-inf')

        if memo_contri.get(node) is not None:
            return memo_contri.get(node)
        
        max_contri = max(node.val, node.val + self.contribution(node.left, memo_contri) , node.val + self.contribution(node.right, memo_contri))
        
        memo_contri[node] = max_contri
        return max_contri

    def individual(self, node, memo_ind, memo_contri):
        if node is None:
            return float('-inf')
        
        if memo_ind.get(node) is not None:
            return memo_ind.get(node)
        
        maxi = max(
            node.val,
            self.individual(node.left, memo_ind, memo_contri),  
            self.individual(node.right, memo_ind, memo_contri),  
            node.val + self.contribution(node.left, memo_contri),
            node.val + self.contribution(node.right, memo_contri),
            node.val + self.contribution(node.left, memo_contri) + self.contribution(node.right, memo_contri) 
        )
        memo_ind[node] = maxi
        return maxi

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        memo_ind = {}
        memo_contri = {}
        return self.individual(root, memo_ind, memo_contri)




# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.