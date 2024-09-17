#User function Template for python3
# https://www.geeksforgeeks.org/problems/subset-sums2234/1
class Solution:
	def subsetSums(self, arr, n):
		# code here
        def recurse(curr_index):
            if curr_index == len(arr):
                return [0]
            # 1 * arr[curr_index] + recursion_list and 0 * arr[curr_index] + recursion_list
            curr_sum_arr = recurse(curr_index+1)
            return [x + arr[curr_index] for x in curr_sum_arr] + curr_sum_arr
		curr_index = 0
		return recurse(curr_index)
