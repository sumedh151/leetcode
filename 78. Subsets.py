class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recurse(curr_index):
            if curr_index == len(nums):
                return [[]]
            curr_subs_arr = recurse(curr_index+1)
            return [x + [nums[curr_index]] for x in curr_subs_arr] + curr_subs_arr
        curr_index = 0
        return recurse(curr_index)
