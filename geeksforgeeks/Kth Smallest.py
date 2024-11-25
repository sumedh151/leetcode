# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1
#User function Template for python3
class Solution:

    def kthSmallest(self, arr,k):
        # arr.sort()
        # return arr[k-1]
        
        import heapq
        heapq.heapify(arr)
        for _ in range(k):
            smallest = heapq.heappop(arr)
        return smallest


# Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
# Output:  7
# Explanation: 3rd smallest element in the given array is 7.



# Input: arr[] = [2, 3, 1, 20, 15], k = 4 
# Output: 15
# Explanation: 4th smallest element in the given array is 15.
