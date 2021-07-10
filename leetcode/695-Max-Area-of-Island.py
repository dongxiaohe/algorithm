class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0: return 0
            grid[i][j] = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            res = 1
            for x, y in directions:
                res += dfs(i + x, j + y)
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: res = max(res, dfs(i, j))
        return res
