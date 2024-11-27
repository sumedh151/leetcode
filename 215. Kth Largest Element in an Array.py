# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # approach 1: O(nlogn)
        # nums.sort(reverse=True)
        # return nums[k-1]

        # # approach 2: using max heap
        # # TC: O(n + klogn)
        # import heapq
        # heapq._heapify_max(nums)
        # for i in range(k):
        #     largest = heapq._heappop_max(nums)
        # return largest

        # approach 3: using min heap 
        # TC: O(nlogk)
        import heapq
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
        
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
