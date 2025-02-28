# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height , right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return abs(left_height-right_height)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right) 


# Given a binary tree, determine if it is height-balanced.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true