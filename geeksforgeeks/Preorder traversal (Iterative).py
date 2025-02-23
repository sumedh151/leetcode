# https://www.geeksforgeeks.org/problems/preorder-traversal-iterative/1
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# iterative
class Solution:
    # Return a list containing the preorder traversal of the given tree
    def preOrder(self, root):
        # code here
        from collections import deque
        stack = deque()
        curr = root
        iterative_traverse = []
        while(curr or stack):
            if curr:
                iterative_traverse.append(curr.data)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right
        return iterative_traverse    


# Given a Binary tree. Find the preorder traversal of the tree without using recursion.

# Example 1:

# Input:
#            1
#          /   \
#         2     3
#       /  \
#      4    5

# Output: 1 2 4 5 3

# Explanation:
# Preorder traversal (Root->Left->Right) of the tree is 1 2 4 5 3.


# Example 2

# Input:
#             8
#           /   \
#          1      5
#           \    /  \
#            7  10   6
#             \  /
#             10 6
# Output: 8 1 7 10 5 10 6 6 

# Explanation:
# Preorder traversal (Root->Left->Right) of the tree is 8 1 7 10 5 10 6 6.
