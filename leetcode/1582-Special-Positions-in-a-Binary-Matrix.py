class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if matrix[i][j]:
                    rows[i] += 1
                    cols[i] += 1
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    res += 1
        return res
            
