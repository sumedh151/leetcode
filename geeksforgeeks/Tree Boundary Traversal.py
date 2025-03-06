# https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    
    def is_leaf(self, node):
        return node.left is None and node.right is None

    
    def collect_left_boundary(self, node, res):
        if node is None or self.is_leaf(node):
            return
        res.append(node.data)
        if node.left:
            self.collect_left_boundary(node.left, res)
        elif node.right:
            self.collect_left_boundary(node.right, res)

    def collect_leaves(self, node, res):
        if node is None:
            return
    
        if self.is_leaf(node):
            res.append(node.data)
            return
    
        self.collect_leaves(node.left, res)
        self.collect_leaves(node.right, res)
        
    def collect_boundary_right(self, node, res):
        if node is None or self.is_leaf(node):
            return
    
        if node.right:
            self.collect_boundary_right(node.right, res)
        elif node.left:
            self.collect_boundary_right(node.left, res)
    
        res.append(node.data)

    def boundaryTraversal(self, root):
        # Code here
        res = []
    
        if not root:
            return res
    
        if not self.is_leaf(root):
            res.append(root.data)
    
        self.collect_left_boundary(root.left, res)
        self.collect_leaves(root, res)
        self.collect_boundary_right(root.right, res)
    
        return res


# Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 
# Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must prefer the left child over the right child when traversing. Do not include leaf nodes in this section.
# Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.
# Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, traversed in reverse order. You must prefer the right child over the left child when traversing. Do not include the root in this section if it was already included in the left boundary.
# Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

# Examples:

# Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
# Output: [1, 2, 4, 8, 9, 6, 7, 3]
# Explanation:

# Input: root[] = [1, 2, N, 4, 9, 6, 5, N, 3, N, N, N, N 7, 8]
# Output: [1, 2, 4, 6, 5, 7, 8]
# Explanation:
# As the root doesn't have a right subtree, the right boundary is not included in the traversal.

# Input: root[] = [1, N, 2, N, 3, N, 4, N, N] 
#     1
#      \
#       2
#        \
#         3
#          \
#           4

# Output: [1, 4, 3, 2]
# Explanation:
# Left boundary: [1] (as there is no left subtree)
# Leaf nodes: [4]
# Right boundary: [3, 2] (in reverse order)
# Final traversal: [1, 4, 3, 2]
