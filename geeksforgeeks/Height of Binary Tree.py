# https://www.geeksforgeeks.org/problems/height-of-binary-tree/1
#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        def recurse(node, curr_height):
            if node == None:
                return curr_height
            left_height = recurse(node.left ,curr_height+1)
            right_height = recurse(node.right ,curr_height+1)
            return max(left_height , right_height)
        return recurse(root,0)-1 # height = level-1

class Solution:
    def height(self, root):
        def recurse(node):
            if node == None:
                return 0
            left_height = recurse(node.left)
            right_height = recurse(node.right)
            return max(left_height , right_height)+1
        return recurse(root)-1 # height = level-1
        
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
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
                    traverse[level].append(node.data)
                else:
                    traverse[level].append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level - 1 #height is level-1


# Given a binary tree, find its height.
# The height of a tree is defined as the number of edges on the longest path from the root to a leaf node. A leaf node is a node that does not have any children.

# Examples:

# Input: root[] = [12, 8, 18, 5, 11] 
# Output: 2
# Explanation: One of the longest path from the root (node 12) goes through node 8 to node 5, which has 2 edges.

# Input: root[] = [1, 2, 3, 4, N, N, 5, N, N, 6, 7]  
# Output: 3
# Explanation: The longest path from the root (node 1) to a leaf node 6 with 3 edge.