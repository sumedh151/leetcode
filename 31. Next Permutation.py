class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_point_index = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                break_point_index = i
                break
        
        if break_point_index == -1:
            nums.reverse()
            return
        
        min_ele = float('inf')
        min_ind = -1
        for i in range(break_point_index, len(nums)):
            if nums[i] < min_ele and nums[i] > nums[break_point_index-1]:
                min_ele = nums[i]
                min_ind = i

        nums[min_ind] , nums[break_point_index-1] = nums[break_point_index-1] , nums[min_ind]
        nums[break_point_index: ] = sorted(nums[break_point_index: ])