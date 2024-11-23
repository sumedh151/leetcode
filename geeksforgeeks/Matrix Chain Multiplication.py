# https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        def recurse(i, j):
            if i>=j:
                return 0
            if memo[i][j] !=-1:
                return memo[i][j] 
            min_cost = float('inf')

            for k in range(i,j):

                if memo[i][k] != -1:
                    temp_ans1 = memo[i][k]
                else:
                    temp_ans1 = recurse(i,k)
                    memo[i][k] = temp_ans1

                if memo[k+1][j] != -1:
                    temp_ans2 = memo[k+1][j]
                else:
                    temp_ans2 = recurse(k+1,j)
                    memo[i][k] = temp_ans1

                temp_ans = temp_ans1 + temp_ans2 + (arr[i-1] * arr[k] * arr[j])
                memo[i][j] = temp_ans
                min_cost = min(min_cost , temp_ans)
            return min_cost
            
        memo = [[-1 for _ in range(len(arr) + 1)] for _ in range(len(arr) + 1)]
        min_cost = recurse(1 , len(arr)-1)
        return min_cost


# Input: arr[] = [2, 1, 3, 4]
# Output: 20
# Explanation: There are 3 matrices of dimensions 2×1, 1×3, and 3×4, Let the input 3 matrices be M1, M2, and M3. There are two ways to multiply ((M1 x M2) x M3) and (M1 x (M2 x M3)), Please note that the result of M1 x M2 is a 2 x 3 matrix and result of (M2 x M3) is a 1 x 4 matrix.
# ((M1 x M2) x M3)  requires (2 x 1 x 3)  + (0) +  (2 x 3 x 4) = 30 
# (M1 x (M2 x M3))  requires (0)  + (1 x 3 x 4) +  (2 x 1 x 4) = 20 
# The minimum of these two is 20.


# Input: arr[] = [1, 2, 3, 4, 3]
# Output: 30
# Explanation: There are 4 matrices of dimensions 1×2, 2×3, 3×4, 4×3. Let the input 4 matrices be M1, M2, M3 and M4. The minimum number of multiplications are obtained by ((M1M2)M3)M4. The minimum number is 1*2*3 + 1*3*4 + 1*4*3 = 30.


# Input: arr[] = [3, 4]
# Output: 0
# Explanation: As there is only one matrix so, there is no cost of multiplication.



# without memoization
#User function Template for python3

class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        def recurse(i, j):
            if i>=j:
                return 0
            min_cost = float('inf')
            for k in range(i,j):
                temp_ans = recurse(i,k) + recurse(k+1,j) + (arr[i-1] * arr[k] * arr[j])
                min_cost = min(min_cost , temp_ans)
            return min_cost
        min_cost = recurse(1 , len(arr)-1)
        return min_cost	