# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # using stack + queue
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            traversal.append([])
            for _ in range(curr_len):
                node = q.popleft()
                if not mirror:
                    traversal[level].append(node.val)
                else:
                    stack.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if mirror:
                while stack:
                    traversal[level].append(stack.pop())
            level+=1
        return traversal


    # using deque
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            traversal.append([])
            for _ in range(curr_len):
                if not mirror:
                    node = dq.popleft()
                else:
                    node = dq.pop()
                traversal[level].append(node.val)
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


# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []