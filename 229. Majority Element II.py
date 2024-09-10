class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        curr_ele1 = None
        curr_ele2 = None
        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums)):
            if cnt1 == 0 and nums[i] != curr_ele2:
                curr_ele1 = nums[i]
                cnt1+=1
            elif cnt2 == 0 and nums[i] != curr_ele1:
                curr_ele2 = nums[i]
                cnt2+=1
            elif curr_ele1 == nums[i]:
                cnt1+=1
            elif curr_ele2 == nums[i]:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1

        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums)):
            if nums[i]==curr_ele1:
                cnt1+=1
            elif nums[i]==curr_ele2:
                cnt2+=1
            else:
                pass

        l = []
        if cnt1>n//3:
            l.append(curr_ele1)
        if cnt2>n//3:
            l.append(curr_ele2)
        return list(set(l))