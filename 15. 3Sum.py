class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sums = []
        # used = []
        # target = 0
        # for i in range(len(nums)):
        #     curr_target = target - nums[i]
        #     target_dict = {}
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         if curr_target - nums[j] in target_dict:
        #             sums.append([
        #                 nums[i], nums[j], nums[target_dict[curr_target - nums[j]]]
        #             ])
        #         else:
        #             target_dict[nums[j]] = j
        # return sums

        nums.sort()
        sums = []
        target = 0
        for i in range(len(nums)):
            curr = nums[i]
            curr_target = target - nums[i]
            left = i+1
            right= len(nums) -1
            if nums[i] == nums[i-1] and i>0:
                continue
            while(left < right):
                if nums[left] == nums[left-1] and left-1 != i:
                    left += 1
                elif right+1 != len(nums) and nums[right] == nums[right+1]:
                    right -= 1
                elif nums[left] + nums[right] == curr_target:
                    sums.append([curr , nums[left] , nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < curr_target:
                    left += 1
                else:
                    right -= 1
        return sums