class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i, j, m, n, oldColor):
            image[i][j] = newColor
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == oldColor:
                    dfs(x, y, m, n, oldColor)
        m, n = len(image), len(image[0])
        if image[sr][sc] != newColor:
            dfs(sr, sc, m, n, image[sr][sc])
        return image
