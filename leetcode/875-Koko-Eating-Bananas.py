class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def countDays(piles, k, h):
            cnt = 0
            for pile in piles:
                cnt += pile // k
                if pile % k != 0:
                    cnt += 1
            return cnt <= h
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l >> 1)
            if countDays(piles, m, h): r = m
            else: l = m + 1
        return l
