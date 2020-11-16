class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        distances = collections.defaultdict(int)
        if len(heights) == 0: return -1
        pq = [(0, (0, 0))]
        while pq:
            current_distance, current_position = heapq.heappop(pq);
            if current_position not in distances:
                distances[current_position] = current_distance
                x, y = current_position
                if x - 1 >= 0:
                    heapq.heappush(pq, (max(current_distance, abs(heights[x - 1][y] - heights[x][y])), (x - 1, y)))
                if x + 1 < len(heights):
                    heapq.heappush(pq, (max(current_distance, abs(heights[x + 1][y] - heights[x][y])), (x + 1, y)))
                if y - 1 >= 0:
                    heapq.heappush(pq, (max(current_distance, abs(heights[x][y - 1] - heights[x][y])), (x, y - 1)))
                if y + 1 < len(heights[0]):
                    heapq.heappush(pq, (max(current_distance, abs(heights[x][y + 1] - heights[x][y])), (x, y + 1)))
        return distances[(len(heights) - 1, len(heights[0]) - 1)]
        

