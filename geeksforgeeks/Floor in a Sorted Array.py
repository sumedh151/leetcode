# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/0
class Solution:
    #User function Template for python3

    #Complete this function
    # # bad , dirty code
    # def findFloor(self,arr,k):
    #     #Your code here
    #     n = len(arr)
    #     left = 0
    #     right = n-1 
    #     while (left<=right):
    #         mid = left + (right-left)//2
    #         if arr[mid]==k:
    #             return mid

    #         if (left==right or right-left==1) and k<arr[left]:
    #             if left>0:
    #                 return left-1
    #             else:
    #                 return -1
    #         elif (left==right or right-left==1) and k>arr[right]:
    #             return right

    #         if k<arr[mid]:
    #             right = mid-1
    #         else:
    #             left = mid+1
    #     return -1

    # my updated solution
    def findFloor(self,arr,k):
        #Your code here
        n = len(arr)
        l = 0
        r = n-1
        while (l<=r):
            mid = l + (r-l)//2
            prev = (mid-1+n)%n
            next_ = (mid+1+n)%n
            if k==arr[mid]:
                return mid
            if k < arr[mid]:
                r = mid-1
            elif k > arr[mid]:
                l = mid+1
        # start checking from next as next largest among 3, !=0 condition is for when mid is last element
        if arr[next_]<k and next_!=0:
            return next_
        elif arr[mid]<k:
            return mid
        elif arr[prev]<k:
            return prev
        return -1

    # av solution
    def findFloor(self,arr,k):
        #Your code here
        n = len(arr)
        left = 0
        right = n-1
        res = -1
        while (left<=right):
            mid = left + (right-left)//2
            if arr[mid]==k:
                return mid

            if arr[mid]<k:
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res

# Examples

# Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 0
# Output: -1
# Explanation: No element less than 0 is found. So output is -1.

# Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 5
# Output: 1
# Explanation: Largest Number less than 5 is 2 , whose index is 1.

# Input: arr[] = [1, 2, 8], k = 1
# Output: 0
# Explanation: Largest Number less than or equal to  1 is 1 , whose index is 0.
