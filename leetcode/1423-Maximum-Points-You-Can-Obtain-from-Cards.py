class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        m = len(cardPoints)
        if k == m: return sum(cardPoints)
        cur = sum(cardPoints[m - k:])
        res, i = cur, 0
        while i < k:
            cur = cur + cardPoints[i] - cardPoints[m - k + i]
            res = max(res, cur)
            i += 1
        return res
