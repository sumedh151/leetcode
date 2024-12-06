# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/0
class Solution:
    #User function Template for python3

    #Complete this function
    def findFloor(self,arr,k):
        #Your code here
        n = len(arr)
        left = 0
        right = n-1 
        while (left<=right):
            mid = left + (right-left)//2
            if arr[mid]==k:
                return mid

            if (left==right or right-left==1) and k<arr[left]:
                if left>0:
                    return left-1
                else:
                    return -1
            elif (left==right or right-left==1) and k>arr[right]:
                return right

            if k<arr[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1


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
