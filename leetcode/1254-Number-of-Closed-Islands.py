class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            res = True
            for x, y in dr:
                res = res & dfs(grid, i + x, j + y)
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0 and dfs(grid, i, j):
                    res += 1
        return res
