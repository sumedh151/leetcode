#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# using 2 stacks
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,node):
        # code here
        from collections import deque
        stack = deque()
        curr = node
        traverse = deque()
        while(stack or curr):
            if curr:
                stack.append(curr)
                traverse.append(curr.data)
                curr = curr.right
            else:
                curr = stack.pop()
                curr = curr.left

        # reversing traverse
        traverse2 = list()
        while(traverse):
            traverse2.append(traverse.pop())
        return traverse2


# using 1 stack
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,node):
        # code here
        from collections import deque
        stack = deque()
        curr = node
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
                    traverse.append(curr.data)
                    curr = None
        return traverse








# Given a binary tree. Find the postorder traversal of the tree without using recursion. Return a list containing the postorder traversal of the tree, calculated without using recursion.

# Examples :

# Input:
#            1
#          /   \
#         2     3
#       /  \
#      4    5

# Output: 4 5 2 3 1
# Explanation: Postorder traversal (Left->Right->Root) of the tree is 4 5 2 3 1.

# Input:
#              8
#           /      \
#         1          5
#          \       /   \
#           7     10    6
#            \   /
#             10 6

# Output: 10 7 1 6 10 6 5 8 
# Explanation: Postorder traversal (Left->Right->Root) of the tree is 10 7 1 6 10 6 5 8 .