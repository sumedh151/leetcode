# https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height , right_height)
        
    def isBalanced(self, root):
        # code here
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return abs(left_height-right_height)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right) 



# Given a binary tree, determine if it is height-balanced. A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree.

# Examples:

# Input: root[] = [10, 20, 30, 40, 60]
# Output: true
# Explanation: The height difference between the left and right subtrees at all nodes is at most 1. Hence, the tree is balanced.

# Input: root[] = [1, 2, 3, 4, N, N, N, 5]   
# Output: false
# Explanation: The height difference between the left and right subtrees at node 2 is 2, which exceeds 1. Hence, the tree is not balanced.

# Input: root[] = [1, 2, N, N, 3]   
# Output: false
# Explanation: The height difference between the left and right subtrees at node 1 is 2, which exceeds 1. Hence, the tree is not balanced.
