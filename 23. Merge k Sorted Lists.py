# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val , i , lists[i]))
        dummy = ListNode()
        tail = dummy   
        while heap:
            _ , i, popped = heapq.heappop(heap)
            tail.next = popped
            tail = tail.next
            if popped.next:
                heapq.heappush(heap, (popped.next.val , i , popped.next))
        return dummy.next



# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []