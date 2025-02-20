# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n-1

        if n==1:
            return 0
        if arr[left]>arr[left+1]:
            return left
        if arr[right]>arr[right-1]:
            return right
        
        while(left<=right):
            mid = left + (right-left)//2

            if (arr[mid] > arr[mid-1]) and (arr[mid] > arr[mid+1]):
                return mid

            if arr[mid]<arr[mid+1]:
                left = mid+1
            else:
                right = mid-1
        return -1


# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
# Return the index of the peak element.
# Your task is to solve it in O(log(n)) time complexity.

# Example 1:
# Input: arr = [0,1,0]
# Output: 1

# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1

