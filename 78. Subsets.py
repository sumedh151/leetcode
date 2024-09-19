# class Solution:
# bad code, dirty code, in operator and all, time complexity calculation difficult and not straight forward
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def recurse(curr_index):
#             if curr_index == len(nums):
#                 return [[]]
#             curr_subs_arr = recurse(curr_index+1)
#             return [x + [nums[curr_index]] for x in curr_subs_arr] + curr_subs_arr
#         curr_index = 0
#         return recurse(curr_index)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recurse(curr_index, curr_subset):
            if curr_index == len(nums):
                subsets.append(curr_subset)
                return
            recurse(curr_index+1, curr_subset + [nums[curr_index]])
            recurse(curr_index+1, curr_subset)
        curr_index = 0
        curr_subset = []
        subsets = []
        recurse(curr_index, curr_subset)
        return subsets
