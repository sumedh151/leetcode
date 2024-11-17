# https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        # recursive solution
        def recurse(n,m):
            if memo[n][m] != -1:
                return memo[n][m]
            if n==0 or m==0:
                return 0
            if text1[n-1] == text2[m-1]:
                memo[n][m] = 1 + recurse(n-1 , m-1)
                return memo[n][m]
            else:
                memo[n][m] = max(recurse(n-1 , m) ,  recurse(n , m-1))
                return memo[n][m]
        n = len(text1)
        m = len(text2)
        memo = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        lcs_len = recurse(n, m)
        return lcs_len



        # iterative solution
        n = len(text1)
        m = len(text2)
        t = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    t[i][j] = 0
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j] ,  t[i][j-1])
        return t[n][m]


# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
