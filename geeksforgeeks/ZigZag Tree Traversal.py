# https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    # queue + stack
    def zigZagTraversal(self, root):
        # Your code here
        from collections import deque
        if root is None:
            return []
        q = deque()
        q.append(root)
        traversal = []
        level = 0
        while(q):
            curr_len = len(q)
            mirror = True if level%2==1 else False
            stack = deque()
            for _ in range(curr_len):
                node = q.popleft()
                if not mirror:
                    traversal.append(node.data)
                else:
                    stack.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if mirror:
                while stack:
                    traversal.append(stack.pop())
            level+=1
        return traversal

    # using deque
    def zigZagTraversal(self, root):
        from collections import deque
        if root is None:
            return []
        dq = deque()
        dq.append(root)
        traversal = []
        level = 0
        while(dq):
            curr_len = len(dq)
            mirror = True if level%2==1 else False
            for _ in range(curr_len):
                if not mirror:
                    node = dq.popleft()
                else:
                    node = dq.pop()
                traversal.append(node.data)
                if not mirror:
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                else:
                    if node.right:
                        dq.appendleft(node.right)
                    if node.left:
                        dq.appendleft(node.left)
            level+=1
        return traversal


# Given a binary tree with n nodes. Find the zig-zag level order traversal of the binary tree.
# In zig zag traversal starting from the first level go from left to right for odd-numbered levels and right to left for even-numbered levels.

# Examples:

# Input:
#         1
#       /   \
#      2      3
#     / \    /  \
#    4   5  6    7
# Output: [1, 3, 2, 4, 5, 6, 7]
# Explanation:
# For level 1 going left to right, we get traversal as {1}.
# For level 2 going right to left, we get traversal as {3,2}.
# For level 3 going left to right, we get traversal as {4,5,6,7}.
# Merging all this traversals in single array we get {1,3,2,4,5,6,7}.

# Input:
#           7
#         /   \
#        9     7
#      /  \   /   
#     8   8  6     
#    /  \
#   10   9 
# Output: [7, 7, 9, 8, 8, 6, 9, 10] 
# Explanation:
# For level 1 going left to right, we get traversal as {7}.
# For level 2 going right to left, we get traversal as {7,9}.
# For level 3 going left to right, we get traversal as {8,8,6}.
# For level 4 going right to left, we get traversal as {9,10}.
# Merging all this traversals in single array we get {7,7,9,8,8,6,9,10}.

# Input:
#           5
#         /   \
#        1     9
#       / \   / \
#      3   2 8   4

# Output: [5, 9, 1, 3, 2, 8, 4]
# Explanation:
# For level 1 going left to right, we get traversal as {5}.
# For level 2 going right to left, we get traversal as {9,1}.
# For level 3 going left to right, we get traversal as {3,2,8,4}.
# Merging all this traversals in single array we get {5,9,1,3,2,8,4}.
