# https://www.geeksforgeeks.org/problems/postorder-traversal/1
#User function Template for python3


'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# recursive
class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        # code here
        def traverse_postorder(node):
            if node is None:
                return []
            res = []
            res.extend(traverse_postorder(node.left))
            res.extend(traverse_postorder(node.right))
            res.append(node.data)
            return res
        
        return traverse_postorder(root)


# Given a binary tree, find the Postorder Traversal of it and return a list containing the postorder traversal of the given tree.

# Examples:

# Input: root = [19, 10, 8, 11, 13]
# Output: [11, 13, 10, 8, 19]

# Input: root = [11, 15, N, 7]
# Output: [7, 15, 11]