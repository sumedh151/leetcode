#Your task is to complete this function
#Your should return the required output
class Solution:
    # https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
    def maxLen(self, n, arr):
        #Code here
        curr_sum = 0
        max_len = 0
        sum_dict = {}
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum==0:
                max_len = i+1
            elif curr_sum in sum_dict:
                max_len = max(i-sum_dict[curr_sum], max_len)
            else:
                sum_dict[curr_sum] = i
        return max_len

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends