# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while(left <= right):
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            if nums[left] <= nums[mid]: #left part sorted
                if (nums[left]<=target and target<=nums[mid]):
                    right = mid -1
                else:
                    left = mid + 1
            elif nums[right] >= nums[mid]: #right part sorted:
                if (nums[right]>=target and target>=nums[mid]):
                    left = mid + 1
                else:
                    right = mid -1
        return -1



# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1
