#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    
    def contribution(self, node, memo_contri):
        if node is None:
            return float('-inf')

        if memo_contri.get(node) is not None:
            return memo_contri.get(node)
        
        max_contri = max(node.data, node.data + self.contribution(node.left, memo_contri) , node.data + self.contribution(node.right, memo_contri))
        
        memo_contri[node] = max_contri
        return max_contri

    def individual(self, node, memo_ind, memo_contri):
        if node is None:
            return float('-inf')
        
        if memo_ind.get(node) is not None:
            return memo_ind.get(node)
        
        maxi = max(
            node.data,
            self.individual(node.left, memo_ind, memo_contri),  
            self.individual(node.right, memo_ind, memo_contri),  
            node.data + self.contribution(node.left, memo_contri),
            node.data + self.contribution(node.right, memo_contri),
            node.data + self.contribution(node.left, memo_contri) + self.contribution(node.right, memo_contri) 
        )
        memo_ind[node] = maxi
        return maxi    

    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        memo_ind = {}
        memo_contri = {}
        return self.individual(root, memo_ind, memo_contri)




# Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

# Examples:

# Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
# Output: 42
# Explanation: Max path sum is represented using green colour nodes in the above binary tree.

# Input: root[] = [-17, 11, 4, 20, -2, 10]
# Output: 31
# Explanation: Max path sum is represented using green colour nodes in the above binary tree.