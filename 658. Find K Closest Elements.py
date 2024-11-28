# https://leetcode.com/problems/find-k-closest-elements/description/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # TC: O(nlogk)
        # TC: O(k)
        import heapq
        max_heap = []
        for i in range(len(arr)):
            diff = abs(x-arr[i])
            heapq.heappush(max_heap, (-diff,-arr[i]))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        k_closest = []
        while(len(max_heap)>0):
            k_closest.append(-heapq.heappop(max_heap)[1])
        return sorted(k_closest)



# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Example 2:
# Input: arr = [1,1,2,3,4,5], k = 4, x = -1
# Output: [1,1,2,3]