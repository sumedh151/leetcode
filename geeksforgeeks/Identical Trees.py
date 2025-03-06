# https://www.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1
#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,r1, r2):
        # Code here
        if r1 is None and r2 is None:
            return True
        if (r1 is None and r2 is not None) or (r1 is not None and r2 is None):
            return False
        return r1.data == r2.data and self.isIdentical(r1.left, r2.left) and self.isIdentical(r1.right, r2.right)


# Given two binary trees with their root nodes r1 and r2, return true if both of them are identical, otherwise, false.

# Examples:

# Input:
#     1          1
#    /   \       /   \
#   2     3    2    3
# Output: true
# Explanation:  There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.

# Input:
#     1         1
#    /   \      /  \
#   2     3   3   2
# Output: false
# Explanation: There are two trees both having 3 nodes and 2 edges, but both trees are not identical.

# Input:
#     1   1
#    /      \
#   2        2
# Output: false
# Explanation: Although both trees have the same node values (1 and 2), they are arranged differently, making the trees non-identical.
