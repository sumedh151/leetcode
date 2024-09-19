class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recurse(curr_index , curr_sum , curr_combination):
            if curr_sum==target:
                combinations.append(curr_combination)
                return
            if curr_sum > target:
                return
            if curr_index == len(candidates):
                return
            recurse(curr_index , curr_sum + candidates[curr_index] , curr_combination + [candidates[curr_index]])
            recurse(curr_index + 1, curr_sum , curr_combination)
            return
        
        curr_index = 0
        curr_sum = 0
        curr_combination = []
        combinations = []
        recurse(curr_index , curr_sum , curr_combination)
        return combinations