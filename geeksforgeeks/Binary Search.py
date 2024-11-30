#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # # Code Here
        # # iterative
        # left = 0
        # right = len(arr)-1
        # result = -1
        # while(left <= right):
        #     # mid = (left+right)//2
        #     mid = left+(right-left)//2
        #     if k == arr[mid]:
        #         result = mid
        #         right = mid - 1 
        #     elif k<arr[mid]:
        #         right = mid - 1 
        #     else:
        #         left = mid + 1
        # return result


        # recursive
        def recurse(left,right):
            if left>right:
                return -1
            # mid = (left+right)//2
            mid = left+(right-left)//2
            if k == arr[mid]:
                if mid == 0 or arr[mid - 1] != k:
                    return mid
                else:
                    return recurse(left, mid - 1)
            elif k<arr[mid]:
                index = recurse(left,mid - 1)
            else:
                index = recurse(mid+1,right)
            return index
        index = recurse(0,len(arr)-1)
        return index


# Examples:

# Input: arr[] = [1, 2, 3, 4, 5], k = 4
# Output: 3
# Explanation: 4 appears at index 3.

# Input: arr[] = [11, 22, 33, 44, 55], k = 445
# Output: -1
# Explanation: 445 is not present.

# Input: arr[] = [1, 1, 1, 1, 2], k = 1
# Output: 0
# Explanation: 1 appears at index 0.
