class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = [False] * len(grid[0])
        res = 0
        for i in range(len(grid)):
            for j in range(len(negatives)):
                if not negatives[j] and grid[i][j] < 0:
                    negatives[j] = True
                    res += (len(grid) - i)
        return res
