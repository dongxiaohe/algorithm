class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def getSoilders(arr) -> int:
            l, r = 0, len(arr)
            while l < r:
                m = l + (r - l >> 1)
                if arr[m] == 0:
                    r = m
                else:
                    l = m + 1
            return l
        heap = []
        for i in range(len(mat)):
            heapq.heappush(heap, [-getSoilders(mat[i]), -i])
            if len(heap) > k:
                heapq.heappop(heap)
        res, k = [0] * k, k - 1
        while k >= 0:
            res[k] = -heappop(heap)[1]
            k -= 1
        return res
