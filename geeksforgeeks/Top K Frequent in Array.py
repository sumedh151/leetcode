# https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1
#User function Template for python3
class Solution:
    def topKFrequent(self, arr, k):
        #Code here
        # TC: O(nlogk)
        # SC: O(k)
        from collections import Counter
        import heapq
        count = Counter(arr)
        min_heap = []
        for key,value in count.items():
            heapq.heappush(min_heap,(value,key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        k_freq = []
        while(len(min_heap)>0):
            k_freq.append(heapq.heappop(min_heap)[1])
        return list(reversed(k_freq))


# Examples:

# Input: arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
# Output: [4, 1]
# Explanation: Frequency of 4 = 2, Frequency of 1 = 2. These two have the maximum frequency and 4 is larger than 1.

# Input: arr[] = [7, 10,11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
# Output: [5, 11, 7, 10]
# Explanation: Frequency of 5 = 3, Frequency of 11 = 2, Frequency of 7 = 2, Frequency of 10 = 1. These four have the maximum frequency and 5 is largest among rest.
