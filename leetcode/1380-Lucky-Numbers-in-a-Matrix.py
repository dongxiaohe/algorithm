class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        def column(matrix, i):
            return [row[i] for row in matrix]
        res = []
        for i in range(len(matrix)):
            minIndex = matrix[i].index(min(matrix[i]))
            columns = column(matrix, minIndex)
            maxIndex = columns.index(max(columns))
            if maxIndex == i:
                res.append(matrix[i][minIndex])
        return res

