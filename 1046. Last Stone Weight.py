# https://leetcode.com/problems/last-stone-weight/description/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        max_heap = []
        for i in range(len(stones)):
            heapq.heappush(max_heap, -stones[i])
        while(len(max_heap)>1):
            a = -heapq.heappop(max_heap)
            b = -heapq.heappop(max_heap)
            if a-b>0:
                heapq.heappush(max_heap, -(a-b))
        return -heapq.heappop(max_heap) if len(max_heap) else 0



# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

# Example 2:
# Input: stones = [1]
# Output: 1
