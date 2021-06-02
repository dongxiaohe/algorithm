class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = l + (r - l >> 1)
            flow, cnt = 0, 0
            for a in bloomDay:
                flow = 0 if a > mid else flow + 1
                if flow == k:
                    cnt += 1
                    flow = 0
                if cnt == m: break
            if cnt == m: r = mid
            else: l = mid + 1
        return l
