# https://www.geeksforgeeks.org/problems/sum-of-elements-between-k1th-and-k2th-smallest-elements3133/1
#User function Template for python3

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        import heapq
        max_heap1 = []
        max_heap2 = []
        for i in range(N):
            heapq.heappush(max_heap1, -A[i])
            if len(max_heap1) > K1:
                heapq.heappush(max_heap2, heapq.heappop(max_heap1))
            if len(max_heap2) > K2-K1-1:
                heapq.heappop(max_heap2)
        return -sum(max_heap2)


# Example 1:
# Input:
# N  = 7
# A[] = {20, 8, 22, 4, 12, 10, 14}
# K1 = 3, K2 = 6
# Output:
# 26
# Explanation:
# 3rd smallest element is 10
# 6th smallest element is 20
# Element between 10 and 20 
# 12,14. Their sum = 26.
 

# Example 2:
# Input
# N = 6
# A[] = {10, 2, 50, 12, 48, 13}
# K1= 2, K2 = 6
# Output:
# 73
