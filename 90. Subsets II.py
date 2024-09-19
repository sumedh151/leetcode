class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def recurse(curr_index, curr_subset):
            if curr_index == len(nums):
                subsets.append(curr_subset)
                return
            if nums[curr_index] == nums[curr_index-1] and curr_index>0 and len(subsets)>0 and subsets[-1][-1]==nums[curr_index]:
                recurse(curr_index+1, curr_subset)
            else:
                recurse(curr_index+1, curr_subset + [nums[curr_index]])
                recurse(curr_index+1, curr_subset)
        
        nums.sort()
        curr_index = 0
        curr_subset = []
        subsets = []
        recurse(curr_index, curr_subset)
        return subsets