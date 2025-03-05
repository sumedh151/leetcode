# https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1
'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def diameter(self, root):
        # Your code here
        def height(node):
            if node in height_memo:
                return height_memo[node]
            if node is None:
                return 0
            height_memo[node] = 1 + max(height(node.left) , height(node.right))
            return height_memo[node]

        def max_diameter(node):
            if node in max_diam_memo:
                return max_diam_memo[node]
            if node is None:
                return 0
            max_diam_memo[node] = max(max_diameter(node.left) , max_diameter(node.right) , height(node.left) + height(node.right))                
            return max_diam_memo[node]
        
        height_memo = {}
        max_diam_memo = {}
        
        if root is None:
            return 0
        return max_diameter(root)


# Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

# Examples:

# Input: root[] = [1, 2, 3]
# Output: 2
# Explanation: The longest path has 2 edges (node 2 -> node 1 -> node 3).

# Input: root[] = [5, 8, 6, 3, 7, 9]
# Output: 4
# Explanation: The longest path has 4 edges (node 3 -> node 8 -> node 5 -> node 6 -> node 9).