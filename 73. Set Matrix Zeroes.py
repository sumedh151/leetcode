class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0]) if row_len else 0
        
        rows = set()
        columns = set()
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        for i in range(row_len):
            for j in range(col_len):
                if i in rows:
                    matrix[i][:] = [0] * col_len
                    break
                if j in columns:
                    matrix[i][j] = 0