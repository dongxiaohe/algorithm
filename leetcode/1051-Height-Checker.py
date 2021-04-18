class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]: cnt += 1
        return cnt
