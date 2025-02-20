# https://www.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1
#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
        n = len(arr)
        left = 0
        right = n-1

        if n==1:
            return 0
        if arr[left]>arr[left+1]:
            return arr[left]
        if arr[right]>arr[right-1]:
            return arr[right]
        
        while(left<=right):
            mid = left + (right-left)//2

            if (arr[mid] > arr[mid-1]) and (arr[mid] > arr[mid+1]):
                return arr[mid]

            if arr[mid]<arr[mid+1]:
                left = mid+1
            else:
                right = mid-1
        return -1


# Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, 
# find the bitonic point, that is the maximum element in the array.

# Examples:

# Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
# Output: 8
# Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 50
# Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.

# Input: arr[] = [120, 100, 80, 20, 0]
# Output: 120
# Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].
