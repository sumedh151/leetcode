# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node in height_memo:
                return height_memo[node]
            if node is None:
                return 0
            height_memo[node] = 1 + max(height(node.left) , height(node.right))
            return height_memo[node]

        def max_diameter(node):
            if node in max_diam_memo:
                return max_diam_memo[node]
            if node is None:
                return 0
            max_diam_memo[node] = max(max_diameter(node.left) , max_diameter(node.right) , height(node.left) + height(node.right))                
            return max_diam_memo[node]
        
        height_memo = {}
        max_diam_memo = {}
        
        if root is None:
            return 0
        return max_diameter(root)




# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them. 

# Example 1:

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1
