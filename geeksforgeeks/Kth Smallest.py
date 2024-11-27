# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1
#User function Template for python3
class Solution:

    def kthSmallest(self, arr,k):
        # # approach 1: O(nlogn)
        # arr.sort()
        # return arr[k-1]
        
        # # approach 2: using min heap
        # # TC: O(n + klogn)
        # import heapq
        # heapq.heapify(arr)
        # for _ in range(k):
        #     smallest = heapq.heappop(arr)
        # return smallest

        # approach 3: using max heap 
        # TC: O(nlogk)
        heap = []
        import heapq
        for i in range(len(arr)):
            heapq.heappush(heap, -arr[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return -heapq.heappop(heap)



# Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
# Output:  7
# Explanation: 3rd smallest element in the given array is 7.



# Input: arr[] = [2, 3, 1, 20, 15], k = 4 
# Output: 15
# Explanation: 4th smallest element in the given array is 15.
