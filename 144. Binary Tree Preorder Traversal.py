# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursive_preorder_traverse(node):
            if node is None:
                return []
            res = []
            res.append(node.val)
            res.extend(recursive_preorder_traverse(node.left))
            res.extend(recursive_preorder_traverse(node.right))
            return res
        return recursive_preorder_traverse(root)

# iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative
        from collections import deque
        stack = deque()
        curr = root
        iterative_traverse = []
        while(curr or stack):
            if curr:
                iterative_traverse.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right
        return iterative_traverse    


# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [1,2,4,5,6,7,3,8,9]

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]