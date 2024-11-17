# https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1

#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, str1, str2):

        # code here
        
        # soln 1 - recursive
        def recurse(n,m):
            if memo[n][m] != -1:
                return memo[n][m]
            if n==0 or m==0:
                return 0
            if str1[n-1] == str2[m-1]:
                memo[n][m] = 1 + recurse(n-1 , m-1)
                return memo[n][m]
            else:
                memo[n][m] = max(recurse(n-1 , m) ,  recurse(n , m-1))
                return memo[n][m]
        memo = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        lcs_len = recurse(n, m)
        return lcs_len
        
        
        
        # soln 2 - iterative
        t = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    t[i][j] = 0
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j] ,  t[i][j-1])
        return t[n][m]


# Input: n = 6, str1 = ABCDGH and m = 6, str2 = AEDFHR
# Output: 3
# Explanation: LCS for input strings “ABCDGH” and “AEDFHR” is “ADH” of length 3.

# Input: n = 3, str1 = ABC and m = 2, str2 = AC
# Output: 2
# Explanation: LCS of "ABC" and "AC" is "AC" of length 2.

# Input: n = 4, str1 = XYZW and m = 4, str2 = XYWZ
# Output: 3
# Explanation: There are two common subsequences of length 3 “XYZ”, and”XYW”, and no common subsequence. of length more than 3.
