# https://www.geeksforgeeks.org/problems/subset-sums2234/1
# User function Template for python3
# class Solution:
#     # bad way to write code, here we are list from leaf is returned and 
#     # then number is added to each element of the list
#     # time complexity calculation is tough, in operator and all
#   def subsetSums(self, arr, n):
#       # code here
#         def recurse(curr_index):
#             if curr_index == len(arr):
#                 return [0]
#             # 1 * arr[curr_index] + recursion_list and 0 * arr[curr_index] + recursion_list
#             curr_sum_arr = recurse(curr_index+1)
#             return [x + arr[curr_index] for x in curr_sum_arr] + curr_sum_arr
#       curr_index = 0
#       return recurse(curr_index)

class Solution:
    def subsetSums(self, arr, n):
        # code here
        def recurse(curr_index, sum):
            if curr_index == len(arr):
                sum_list.append(sum)
                return
            recurse(curr_index+1, sum)
            recurse(curr_index+1, sum+arr[curr_index])
        curr_index = 0
        sum = 0
        sum_list = []
        recurse(curr_index, sum)
        return sum_list
