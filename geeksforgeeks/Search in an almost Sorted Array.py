# https://www.geeksforgeeks.org/problems/search-in-an-almost-sorted-array/1
#User function Template for python3
class Solution:
    # # bad dirty solution
    # def findTarget(self, arr, target):
    #     # Your code here
    #     n=len(arr)
    #     left = 0
    #     right = n-1
    #     while(left<=right):
    #         mid=left+(right-left)//2
            
    #         # finding actual mid
    #         if arr[mid] == target:
    #             return mid
    #         if mid!=0 and arr[mid - 1] > arr[mid]:
    #             actual_mid_ind = mid - 1
    #         elif mid!=n-1 and arr[mid + 1] < arr[mid]:
    #             actual_mid_ind = mid + 1
    #         else:
    #             actual_mid_ind = mid
            
    #         # reducing search space in terms of actual mid
    #         if target==arr[actual_mid_ind]:
    #             return actual_mid_ind
    #         elif target<=arr[actual_mid_ind]:
    #             right = mid-1
    #         elif target>=arr[actual_mid_ind]:
    #             left = mid+1
    #     return -1

    # clearner, better solution
    def findTarget(self, arr, target):
        # Your code here
        n = len(arr)
        l = 0
        r = n-1
        while (l<=r):
            mid = l + (r-l)//2
            prev = (mid-1+n)%n
            next_ = (mid+1+n)%n
            if target==arr[mid]:
                return mid
            elif target==arr[prev]:
                return prev
            elif target==arr[next_]:
                return next_
                
            if target < arr[mid]:
                r = mid-1
            elif target > arr[mid]:
                l = mid+1
        return -1

# Examples:
# Input: arr[] = [10, 3, 40, 20, 50, 80, 70], target = 40
# Output: 2
# Explanation: Index of 40 in the given array is 2.

# Input: arr[] = [10, 3, 40, 20, 50, 80, 70], target = 90
# Output: -1
# Explanation: 90 is not present in the array.

# Input: arr[] = [-20], target = -20
# Output: 0
# Explanation: -20 is the only element present in the array.