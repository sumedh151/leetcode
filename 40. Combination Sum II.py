class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def recurse(curr_index , curr_sum , curr_combination , last_taken):
            if curr_sum==target:
                combinations.append(curr_combination)
                return
            if curr_sum > target:
                return
            if curr_index == len(candidates):
                return
            if curr_index>0 and candidates[curr_index]==candidates[curr_index-1]:
                if last_taken == False:
                    recurse(curr_index + 1, curr_sum , curr_combination, False)
                    return

            recurse(curr_index + 1 , curr_sum + candidates[curr_index] , curr_combination + [candidates[curr_index]], True)
            recurse(curr_index + 1, curr_sum , curr_combination, False)
            return
        
        candidates.sort()
        print(candidates)
        curr_index = 0
        curr_sum = 0
        curr_combination = []
        combinations = []
        recurse(curr_index , curr_sum , curr_combination, False)
        return combinations