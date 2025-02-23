# https://www.geeksforgeeks.org/problems/level-order-traversal/1
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""

# recursive
class Solution:
    def levelOrder(self, root):
        # Your code here
        def levelOrderCall(node, level):
            if node is None:
                return
            if len(traverse) < level+1:
                traverse.append([])
                traverse[level].append(node.data)
            else:
                traverse[level].append(node.data)
                
            levelOrderCall(node.left, level+1)
            levelOrderCall(node.right, level+1)
            return
        traverse = []
        levelOrderCall(root, 0)
        return traverse

# iterative
class Solution:
    def levelOrder(self, root):
        # Your code here
        from collections import deque
        
        q = deque()
        q.append(root)
        level = 0
        traverse = []
        while (q):
            for _ in range(len(q)):
                node = q.popleft()
                if len(traverse)<level+1:
                    traverse.append([])
                    traverse[level].append(node.data)
                else:
                    traverse[level].append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return traverse
                
# Given a root of a binary tree with n nodes, the task is to find its level order traversal. Level order traversal of a tree is breadth-first traversal for the tree.

# Examples:

# Input: root[] = [1, 2, 3]
# Output: [[1], [2, 3]]

# Input: root[] = [10, 20, 30, 40, 50]
# Output: [[10], [20, 30], [40, 50]]

# Input: root[] = [1, 3, 2, N, N, N, 4, 6, 5]
# Output: [[1], [3, 2], [4], [6, 5]]