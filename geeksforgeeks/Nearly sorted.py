# https://www.geeksforgeeks.org/problems/nearly-sorted-1587115620/1
#User function Template for python3

class Solution:
    def nearlySorted(self, arr, k):
        #code
        # # approach 1
        # # TC: O(nlogn)
        # # SC: O(1)
        # arr.sort()
        # return arr
        
        # approach 2
        # TC: O(nlogk)
        # SC: O(k)
        import heapq
        i = 0
        heap = []
        for j in range(len(arr)):
            heapq.heappush(heap, arr[j])
            if len(heap)>k:
                arr[i] = heapq.heappop(heap)
                i+=1
        while(len(heap)>0):
            arr[i] = heapq.heappop(heap)
            i+=1
        return arr

# Input: arr[] = [6, 5, 3, 2, 8, 10, 9], k = 3
# Output: [2, 3, 5, 6, 8, 9, 10]
# Explanation: The sorted array will be 2 3 5 6 8 9 10

# Input: arr[]= [1, 4, 5, 2, 3, 6, 7, 8, 9, 10], k = 2
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Explanation: The sorted array will be 1 2 3 4 5 6 7 8 9 10
