# https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1
#User function Template for python3

#################################
####### recursive + memo ########
#################################

class Solution:
    def knapSack(self, capacity, val, wt):
        # code here
        def ks(n,cap):
            if memo[n][cap] != -1:
                return memo[n][cap]
            if (n==0 or cap==0):
                return 0
            if (wt[n-1] <= cap):
                selecting = val[n-1] + ks(n, cap - wt[n-1])
                not_selecting = ks(n-1, cap)
                memo[n][cap] = max(selecting , not_selecting)
                return memo[n][cap]
            else:
                memo[n][cap] = ks(n-1,cap)
                return memo[n][cap]
        
        n = len(val)                
        memo = [[-1 for _ in range(capacity+1)] for _ in range(n+1)]
        max_profit = ks(n , capacity)
        return max_profit

# Input: capacity = 100, val[]  = [1, 30], wt[] = [1, 50]
# Output: 100 

# Input: capacity = 8, val[] = [10, 40, 50, 70], wt[]  = [1, 3, 4, 5]        
# Output : 110



#########################
####### top-down ########
#########################



#User function Template for python3

class Solution:
    def knapSack(self, capacity, val, wt):
        # soln 2 - iterative
        n = len(val)                
        t = [[-1 for _ in range(capacity+1)] for _ in range(n+1) ]
        for i in range(len(t)):
            for j in range(len(t[0])):
                if i == 0 or j == 0:
                    t[i][j] = 0

        for i in range(1,n+1):
            for j in range(1,capacity+1):
                if wt[i-1]<=j:
                    t[i][j] = max(val[i-1] + t[i][j - wt[i-1]],
                                t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]

        return t[n][capacity]