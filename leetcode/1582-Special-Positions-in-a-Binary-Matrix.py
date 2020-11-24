class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and rows[i] == 1 and cols[j] == 1:
                    res += 1
        return res
            
