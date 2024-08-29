class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        if numRows==1:
            return out
        for i in range(1, numRows):
            curr = []
            for j in range(1, len(out[i-1])):
                curr.append(out[i-1][j-1] + out[i-1][j])
            out.append([1] + curr + [1])
        return out