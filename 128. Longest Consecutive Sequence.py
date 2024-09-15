class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        max_len = 0
        for i in range(len(nums)):
            if nums[i]-1 in nums_dict:
                continue
            else:
                curr_len = 1
                ptr = nums[i]
                while(ptr+1 in nums_dict):
                    curr_len += 1
                    ptr += 1
                max_len = max(curr_len, max_len)
        return max_len