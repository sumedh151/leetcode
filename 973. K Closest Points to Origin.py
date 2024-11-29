# https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        max_heap = []
        for i in range(len(points)):
            dist = (points[i][0]**2 + points[i][1]**2)**0.5
            heapq.heappush(max_heap, (-dist,points[i]))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        k_closest = []
        while(len(max_heap)>0):
            k_closest.append(heapq.heappop(max_heap)[1])
        return k_closest


# Example 1:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
