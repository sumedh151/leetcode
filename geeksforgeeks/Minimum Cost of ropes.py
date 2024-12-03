# https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
#User function Template for python3

class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr) -> int:
    
        # code here
        import heapq
        min_heap = []
        for i in range(len(arr)):
            heapq.heappush(min_heap, arr[i])
        curr_cost = 0
        while(len(min_heap) > 1):
            a = heapq.heappop(min_heap)
            b = heapq.heappop(min_heap) 
            curr_cost = curr_cost + (a+b)
            heapq.heappush(min_heap, a+b)
        return curr_cost



# Examples:

# Input: arr[] = [4, 3, 2, 6]
# Output: 29
# Explanation: We can connect the ropes in following ways.
# 1) First connect ropes of lengths 2 and 3. Which makes the array [4, 5, 6]. Cost of this operation 2 + 3 = 5. 
# 2) Now connect ropes of lengths 4 and 5. Which makes the array [9, 6]. Cost of this operation 4 + 5 = 9.
# 3) Finally connect the two ropes and all ropes have connected. Cost of this operation 9 + 6 =15. Total cost is 5 + 9 + 15 = 29. This is the optimized cost for connecting ropes. 
# Other ways of connecting ropes would always have same or more cost. For example, if we connect 4 and 6 first (we get three rope of 3, 2 and 10), then connect 10 and 3 (we gettwo rope of 13 and 2). Finally we connect 13 and 2. Total cost in this way is 10 + 13 + 15 = 38.

# Input: arr[] = [4, 2, 7, 6, 9]
# Output: 62 
# Explanation: First, connect ropes 4 and 2, which makes the array [6, 7, 6, 9]. Cost of this operation 4 + 2 = 6. 
# Next, add ropes 6 and 6, which results in [12, 7, 9]. Cost of this operation 6 + 6 = 12.
# Then, add 7 and 9, which makes the array [12,16]. Cost of this operation 7 + 9 = 16. And
# finally, add these two which gives [28]. Hence, the total cost is 6 + 12 + 16 + 28 = 62.

# Input: arr[] = [10]
# Output: 0
# Explanation: Since there is only one rope, no connections are needed, so the cost is 0.
