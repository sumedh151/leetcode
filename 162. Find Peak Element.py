# https://leetcode.com/problems/find-peak-element/description/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        if n==1:
            return 0
        if nums[left]>nums[left+1]:
            return left
        if nums[right]>nums[right-1]:
            return right
        
        while(left<=right):
            mid = left + (right-left)//2

            if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
                return mid

            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
        return -1


# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
