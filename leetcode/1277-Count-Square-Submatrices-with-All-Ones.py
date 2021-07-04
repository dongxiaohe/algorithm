class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        val = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + matrix[i][j]
                        res += val
                        matrix[i][j] = val
        return res
