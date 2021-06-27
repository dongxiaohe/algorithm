class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # evaluate y1 + y2 + |x1 - x2|
        # since x2 > x1 so we can only evaulate y1 - x1 when iterate x2, y2
        pq, res = [], float("-inf")
        for x, y in points:
            while pq and x - pq[0][1] > k:
                heapq.heappop(pq)
            if pq: res = max(res, -pq[0][0] + x + y)
            heapq.heappush(pq, [x - y, x])
        return res
