class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        _min, res = float("inf"), -1
        for i in range(len(points)):
            _x, _y = points[i]
            if x == _x or y == _y:
                distance = abs(x - _x) + abs(y - _y)
                if _min > distance:
                    _min = distance
                    res = i
        return res
