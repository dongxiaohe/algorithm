class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # evaluate y1 + y2 + |x1 - x2|
        # since x2 > x1 so we can only evaulate y1 - x1 when iterate x2, y2
        q, res = collections.deque(), float("-inf")
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                res = max(res, q[0][0] + x + y)
            while q and q[-1][0] < y - x:
                q.pop()
            q.append([y - x, x])
        return res

