class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse=True)
        # return nums[k-1]

        import heapq
        # heapq.heapify(nums)
        heapq._heapify_max(nums)
        for i in range(k):
            # largest = heapq.heappop(nums)
            largest = heapq._heappop_max(nums)
        return largest

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
