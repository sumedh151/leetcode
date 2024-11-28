# https://www.geeksforgeeks.org/problems/k-largest-elements4206/1
#User function Template for python3
class Solution:

	def kLargest(self,arr, k):
		# code here
        # arr.sort()
		# arr.sort(reverse=True)
		# return arr[:k]

        # # approach 2: using max heap
        # # TC: O(n + klogn)
        # # SC: O(k)
		# import heapq
		# heapq._heapify_max(arr)
		# k_largest = []
		# for i in range(k):
		#     k_largest.append(heapq._heappop_max(arr))
		# return k_largest

        # approach 3: using min heap 
        # TC: O(nlogk + k)
        # SC: O(k)
        import heapq
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, arr[i])
            if len(heap) > k:
                heapq.heappop(heap)
        output = []
        while(len(heap) > 0):
            output.append(heapq.heappop(heap))
        return output[::-1]


# Input: arr[] = [12, 5, 787, 1, 23], k = 2
# Output: [787, 23]
# Explanation: 1st largest element in the array is 787 and second largest is 23.

# Input: arr[] = [1, 23, 12, 9, 30, 2, 50], k = 3 
# Output: [50, 30, 23]
# Explanation: Three Largest elements in the array are 50, 30 and 23.

# Input: arr[] = [12, 23], k = 1
# Output: [23]
# Explanation: 1st Largest element in the array is 23.
