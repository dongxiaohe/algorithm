class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res, kv = 0, collections.defaultdict(int)
        i, j = 0, 0
        while i < len(mat) and j < len(mat[0]):
            res += mat[i][j]
            kv[(i, j)] = 1
            i += 1
            j += 1
        i, j = len(mat) - 1, 0
        while i >= 0 and j < len(mat[0]):
            if (i, j) not in kv:
                res += mat[i][j]
            i -= 1
            j += 1
        return res
