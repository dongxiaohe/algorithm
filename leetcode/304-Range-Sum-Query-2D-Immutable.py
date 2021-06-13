class NumMatrix(object):
    def __init__(self, matrix):
        n = len(matrix) + 1
        m = len(matrix[0]) + 1
        self.acc = [[0 for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.acc[i + 1][j + 1] = -self.acc[i][j] + self.acc[i + 1][j] + self.acc[i][j + 1] + matrix[i][j]
    def sumRegion(self, row1, col1, row2, col2):
        return self.acc[row2 + 1][col2 + 1] - self.acc[row2 + 1][col1] - self.acc[row1][col2 + 1] + self.acc[row1][col1]
