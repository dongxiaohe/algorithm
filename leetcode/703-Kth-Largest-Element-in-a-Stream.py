class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = nums
        self.k = k
        heapify(self.pq)
        while len(self.pq) > k: # non inclusive
            heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heappush(self.pq, val)
        elif val > self.pq[0]:
            heapreplace(self.pq, val)
        return self.pq[0]
