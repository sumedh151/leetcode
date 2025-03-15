# https://leetcode.com/problems/find-median-from-data-stream/description/

class MedianFinder:
    import heapq

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.max_heap , -num)        

        # median in first half
        elif len(self.min_heap)<len(self.max_heap):
            median = -self.max_heap[0]
            if num >= median:
                heapq.heappush(self.min_heap , num)        
            else:
                heapq.heappush(self.max_heap , -num)        
                heapq.heappush(self.min_heap , -heapq.heappop(self.max_heap))

        # median in second half
        elif len(self.min_heap)>len(self.max_heap):
            median = self.min_heap[0]
            if num <= median:
                heapq.heappush(self.max_heap , -num)
            else:
                heapq.heappush(self.min_heap , num)
                heapq.heappush(self.max_heap , -heapq.heappop(self.min_heap))
        else:
            median = (self.min_heap[0]-self.max_heap[0])/2
            if num <= median:
                heapq.heappush(self.max_heap , -num)
            else:
                heapq.heappush(self.min_heap , num)
                
    def findMedian(self) -> float:
        # median in first half
        if len(self.min_heap)<len(self.max_heap):
            return -self.max_heap[0]
        # median in second half
        elif len(self.min_heap)>len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0]-self.max_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
