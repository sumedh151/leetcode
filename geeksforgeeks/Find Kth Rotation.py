# https://www.geeksforgeeks.org/problems/rotation4723/1
def findKRotation(self, arr):
    # code here
    # tc: O(logn)
    # sc: O(1)
    n = len(arr)
    left = 0
    right = n-1
    while(left <= right):
        mid = left + (right-left)//2
        prev = (mid+n-1)%n
        next = (mid+1)%n
        if arr[mid]<arr[prev] and arr[mid]<arr[next]:
            return mid
        elif arr[mid]<arr[0]:
            right = mid - 1
        elif arr[mid]>arr[n-1]:
            left = mid + 1
        else:
            return 0


# Examples:

# Input: arr = [5, 1, 2, 3, 4]
# Output: 1
# Explanation: The given array is 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.

# Input: arr = [1, 2, 3, 4, 5]
# Output: 0
# Explanation: The given array is not rotated.
