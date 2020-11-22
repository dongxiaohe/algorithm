class Solution(object):
    _product = -1
    @lru_cache(None)
    def maxProductPath(self, grid):
        def _dfs(i, j, grid, result):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                self._product = max(self._product, result)
                return
            if grid[i][j] == 0:
                self._product = max(self._product, 0)
                return
            if i < len(grid) - 1: _dfs(i + 1, j, grid, result * grid[i + 1][j])
            if j < len(grid[0]) - 1: _dfs(i, j + 1, grid, result * grid[i][j + 1])
        _dfs(0, 0, grid, grid[0][0])
        return self._product % (10 ** 9 + 7) if self._product >= 0 else -1
