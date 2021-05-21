class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < len(res) and j < len(res[0]):
                    res[i][j] = matrix[j][i]
                if j < len(res) and i < len(res[0]):
                    res[j][i] = matrix[i][j]
        return res
