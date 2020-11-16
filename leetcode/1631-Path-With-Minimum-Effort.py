class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        pq = [(0, 0, 0)] # distance, row, col
        distances = collections.defaultdict(int)
        DIR = [0, 1, 0, -1, 0]
        while pq:
            distance, x, y = heapq.heappop(pq)
            if (x, y) not in distances:
                distances[(x, y)] = distance
                for i in range(4):
                    next_x = x + DIR[i]
                    next_y = y + DIR[i + 1]
                    if 0 <= next_x < m and 0 <= next_y < n:
                        heapq.heappush(pq, (max(distance, abs(heights[next_x][next_y] - heights[x][y])), next_x, next_y))
        return distances[(m - 1, n - 1)]
