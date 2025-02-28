# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive 1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(node, curr_height):
            if node == None:
                return curr_height
            left_height = recurse(node.left ,curr_height+1)
            right_height = recurse(node.right ,curr_height+1)
            return max(left_height , right_height)
        return recurse(root,0)

# recursive 2
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            if node == None:
                return 0
            left_height = recurse(node.left)
            right_height = recurse(node.right)
            return max(left_height , right_height)+1
        return recurse(root)

# iterative
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque()
        if root:
            q.append(root)
        else:
            return 0
        level = 0
        traverse = []
        while (q):
            for _ in range(len(q)):
                node = q.popleft()
                if len(traverse)<level+1:
                    traverse.append([])
                    traverse[level].append(node.val)
                else:
                    traverse[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level



# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2