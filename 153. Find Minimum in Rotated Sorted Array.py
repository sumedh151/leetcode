# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # tc: O(logn)
        # sc: O(1)
        n = len(nums)
        left = 0
        right = n-1
        while(left <= right):
            mid = left + (right-left)//2
            prev = (mid-1+n)%n
            next = (mid+1)%n
            if (nums[prev]>nums[mid] and nums[mid]<nums[next]):
                return nums[mid]
            elif nums[0]>nums[mid]:
                right = mid - 1
            elif nums[n-1]<nums[mid]:
                left = mid + 1
            else:
                return nums[0]

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
