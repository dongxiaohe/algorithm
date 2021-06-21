class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, sr, sc, oldColor, newColor, visited):
            image[sr][sc] = newColor
            visited.add((sr, sc))
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newSr, newSc = sr + i, sc + j
                if newSr < 0 or newSr >= len(image) or newSc < 0 or newSc >= len(image[newSr]) or image[newSr][newSc] != oldColor or (newSr, newSc) in visited:
                    continue
                dfs(image, sr + i, sc + j, oldColor, newColor, visited)
        dfs(image, sr, sc, image[sr][sc], newColor, set())
        return image

