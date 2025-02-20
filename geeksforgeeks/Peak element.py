# https://www.geeksforgeeks.org/problems/peak-element/1
#User function Template for python3
class Solution:   
    def peakElement(self,arr):
        # Code here
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



# Examples :

# Input: arr = [1, 2, 4, 5, 7, 8, 3]
# Output: true
# Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].

# Input: arr = [10, 20, 15, 2, 23, 90, 80]
# Output: true
# Explanation: arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6]. 

# Input: arr = [1, 2, 3]
# Output: true
# Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element, so it has negative infinity to its right.
