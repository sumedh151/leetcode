# https://www.geeksforgeeks.org/problems/inorder-traversal/1
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
# '''

# Recursive
class Solution:
    def inOrder(self,root):
        # code here
        def traverse_inorder(node):
            if node is None:
                return []
            res = []
            res.extend(traverse_inorder(node.left))
            res.append(node.data)
            res.extend(traverse_inorder(node.right))
            return res
        
        return traverse_inorder(root)


# Given a Binary Tree, your task is to return its In-Order Traversal.
# left - root - right
# Follow Up: Try solving this with O(1) auxiliary space.

# Examples:

# Input: root[] = [1, 2, 3, 4, 5]       
# Output: [4, 2, 5, 1, 3]
# Explanation: The in-order traversal of the given binary tree is [4, 2, 5, 1, 3].

# Input: root[] = [8, 1, 5, N, 7, 10, 6, N, 10, 6]      
# Output: [1, 7, 10, 8, 6, 10, 5, 6]
# Explanation: The in-order traversal of the given binary tree is [1, 7, 10, 8, 6, 10, 5, 6].
