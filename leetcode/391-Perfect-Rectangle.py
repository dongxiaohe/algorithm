class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = lambda: (y2 - y1) * (x2 - x1)
        cornors = set()
        total = 0
        for x1, y1, x2, y2 in rectangles:
            total += area()
            cornors ^= {(x1, y1), (x2, y1), (x1, y2), (x2, y2)}
        if len(cornors) != 4: return False
        x1, y1 = min(cornors, key = lambda x: x[0] + x[1])
        x2, y2 = max(cornors, key = lambda x: x[0] + x[1])
        return total == area()

