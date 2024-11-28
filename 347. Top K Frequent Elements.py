# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: O(nlogk)
        # SC: O(k)
        from collections import Counter
        import heapq
        count = Counter(nums)
        min_heap = []
        for key,value in count.items():
            heapq.heappush(min_heap,(value,key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        k_freq = []
        while(len(min_heap)>0):
            k_freq.append(heapq.heappop(min_heap)[1])
        return k_freq


# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]