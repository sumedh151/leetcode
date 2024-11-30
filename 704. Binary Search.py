# https://leetcode.com/problems/binary-search/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # iterative
        # left = 0
        # right = len(nums)-1
        # while(left <= right):
        #     # mid = (left+right)//2
        #     mid = left+(right-left)//2
        #     print(left, right, mid, nums[mid], target)
        #     if target == nums[mid]:
        #         return mid
        #     elif target<nums[mid]:
        #         right = mid - 1 
        #     else:
        #         left = mid + 1
        # return -1


        # recursive
        def recurse(left,right):
            if left>right:
                return -1
            # mid = (left+right)//2
            mid = left+(right-left)//2
            if target == nums[mid]:
                return mid
            elif target<nums[mid]:
                index = recurse(left,mid - 1)
            else:
                index = recurse(mid+1,right)
            return index
        index = recurse(0,len(nums)-1)
        return index


# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

