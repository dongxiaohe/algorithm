class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        def equation(x1, y1, x2, y2, k):
            if x2 - x1 <= k:
                return y1 + y2 + x2 - x1
            return float("-inf")
        _max = float("-inf")
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                _max = max(_max, equation(x1, y1, x2, y2, k))
        return _max
