# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n-1
        while(left <= right):
            mid = left + (right-left)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[left] and nums[mid]==nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]: #left part sorted
                if (nums[left]<=target and target<=nums[mid]):
                    right = mid -1
                else:
                    left = mid + 1
            elif nums[right] >= nums[mid]: #right part sorted:
                if (nums[right]>=target and target>=nums[mid]):
                    left = mid + 1
                else:
                    right = mid -1
        return False




# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

