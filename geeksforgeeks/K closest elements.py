# https://www.geeksforgeeks.org/problems/k-closest-elements3619/1
#User function Template for python3

class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        # TC: O(nlogk)
        # SC: O(k)
        import heapq
        max_heap = []
        for i in range(len(arr)-1, -1, -1):
            diff = abs(x-arr[i])
            if diff==0:
                continue
            heapq.heappush(max_heap, (-diff,arr[i]))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        k_closest = []
        while(len(max_heap)>0):
            k_closest.append(heapq.heappop(max_heap)[1])
        return k_closest[::-1]


# Example 1:
# Input:
# n = 13
# arr[] = {12, 16, 22, 30, 35, 39, 42, 
#          45, 48, 50, 53, 55, 56}
# k = 4, x = 35
# Output: 39 30 42 45
# Explanation: 
# First closest element to 35 is 39.
# Second closest element to 35 is 30.
# Third closest element to 35 is 42.
# And fourth closest element to 35 is 45.

# Example 2:
# Input:
# n = 5
# arr[] = {1, 2, 3, 6, 10}
# k = 3, x = 4
# Output: 3 6 2
# Explanation: 
# First closest element is 3.
# There are two elements 2 and 6 for which 
# the difference with 4 is same i.e. 2.
# So first take greatest number 6 
# then the lower number 2.
