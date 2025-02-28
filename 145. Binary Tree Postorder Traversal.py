# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse_postorder(node):
            if node is None:
                return []
            res = []
            res.extend(traverse_postorder(node.left))
            res.extend(traverse_postorder(node.right))
            res.append(node.val)
            return res
        return traverse_postorder(root)

# iterative - using 2 stacks
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        stack = deque()
        curr = root
        traverse = deque()
        while(stack or curr):
            if curr:
                stack.append(curr)
                traverse.append(curr.val)
                curr = curr.right
            else:
                curr = stack.pop()
                curr = curr.left
        
        # reversing traverse
        traverse2 = list()
        while(traverse):
            traverse2.append(traverse.pop())
        return traverse2


# iterative - using 1 stacks
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        stack = deque()
        curr = root
        traverse = []
        while (stack or curr):
            if curr:
                stack.append(curr)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                top = stack[-1] if stack else None
                if curr == top:
                    curr = curr.right
                else:
                    traverse.append(curr.val)
                    curr = None
        return traverse


# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]