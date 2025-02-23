# https://www.geeksforgeeks.org/problems/inorder-traversal-iterative/1
#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
class Solution:
    def inOrder(self, root):
        # code here
        from collections import deque
        stack = deque()
        curr = root
        traverse = []
        while(stack or curr):
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                traverse.append(curr.data)
                curr = curr.right
        return traverse



# Given a binary tree. Find the inorder traversal of the tree without using recursion.

# Example 1

# Input:
#            1
#          /    \
#        2       3
#       /   \
#     4     5
# Output: 4 2 5 1 3

# Explanation:
# Inorder traversal (Left->Root->Right) of  the tree is 4 2 5 1 3.


# Example 2

# Input:
#             8
#           /   \
#             1      5
#              \    /  \
#              7   10   6
#              \  /
#           10 6
# Output: 1 7 10 8 6 10 5 6

# Explanation:
# Inorder traversal (Left->Root->Right)  of the tree is 1 7 10 8 6 10 5 6.
