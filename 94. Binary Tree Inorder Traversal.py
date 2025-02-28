# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # code here
        def traverse_inorder(node):
            if node is None:
                return []
            res = []
            res.extend(traverse_inorder(node.left))
            res.append(node.val)
            res.extend(traverse_inorder(node.right))
            return res
        return traverse_inorder(root)

# iterative
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         from collections import deque
#         stack = deque()
#         curr = root
#         traverse = []
#         while(stack or curr):
#             if curr:
#                 stack.append(curr)
#                 curr = curr.left
#             else:
#                 curr = stack.pop()
#                 traverse.append(curr.val)
#                 curr = curr.right
#         return traverse



# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]