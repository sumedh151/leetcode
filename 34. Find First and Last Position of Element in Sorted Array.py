# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        def search(left , right , first_occ = True):
            result = -1
            while(left <= right):
                mid = left+(right-left)//2
                if target == nums[mid]:
                    if first_occ:
                        result = mid
                        right = mid - 1
                    else:
                        result = mid
                        left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1
            return result
        return [search(left,right,first_occ=True) , search(left,right,first_occ=False)]


# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
