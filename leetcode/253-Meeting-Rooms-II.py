class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        pq = []
        for x, y in intervals:
            if pq and x >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, y)
        return len(pq)
