class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        total_len = m*n
        left = 0
        right = total_len - 1
        while(left <= right):
            mid = (left+right)//2
            row = mid//n
            col = mid%n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                left = mid + 1
        return False