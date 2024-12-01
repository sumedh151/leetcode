# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
class Solution:
    def countFreq(self, arr, target):
        # #code here
        # # iterative
        # left = 0
        # right = len(arr)-1
        # def search(left , right , first_occ = True):
        #     result = -1
        #     while(left <= right):
        #         mid = left+(right-left)//2
        #         if target == arr[mid]:
        #             if first_occ:
        #                 result = mid
        #                 right = mid - 1
        #             else:
        #                 result = mid
        #                 left = mid + 1
        #         elif target<arr[mid]:
        #             right = mid - 1 
        #         else:
        #             left = mid + 1
        #     return result
        # fo = search(left,right,first_occ=True)
        # lo = search(left,right,first_occ=False)
        # return lo-fo+1 if lo!=-1 else 0

        # recursive
        def recurse(left,right):
            if left>right:
                return 0
            # mid = (left+right)//2
            mid = left+(right-left)//2
            if target == arr[mid]:
                count = 1 + recurse(left, mid-1) + recurse(mid+1, right)
            elif target < arr[mid]:
                count = recurse(left,mid - 1)
            else:
                count = recurse(mid+1,right)
            return count
        count = recurse(0,len(arr)-1)
        return count


# Examples :
# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
# Output: 4
# Explanation: target = 2 occurs 4 times in the given array so the output is 4.

# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
# Output: 0
# Explanation: target = 4 is not present in the given array so the output is 0.

# Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
# Output: 3
# Explanation: target = 12 occurs 3 times in the given array so the output is 3.
