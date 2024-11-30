# https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
#User function Template for python3


class Solution:
    def find(self, arr, x):
        
        # code here
        left = 0
        right = len(arr)-1
        def search(left , right , first_occ = True):
            result = -1
            while(left <= right):
                mid = left+(right-left)//2
                if x == arr[mid]:
                    if first_occ:
                        result = mid
                        right = mid - 1
                    else:
                        result = mid
                        left = mid + 1
                elif x<arr[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1
            return result
        return [search(left,right,first_occ=True) , search(left,right,first_occ=False)]


# Examples:

# Input: arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
# Output: [2, 5]
# Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5

# Input: arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7
# Output: [6, 6]
# Explanation: First and last occurrence of 7 is at index 6

# Input: arr[] = [1, 2, 3], x = 4
# Output: [-1, -1]
# Explanation: No occurrence of 4 in the array, so, output is [-1, -1]
