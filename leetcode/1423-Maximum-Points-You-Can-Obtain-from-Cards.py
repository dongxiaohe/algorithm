class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints): return sum(cardPoints)
        arr = cardPoints[len(cardPoints) - k:] + cardPoints[:k]
        cur = sum(arr[:k])
        res = cur
        i = 0 
        while i < len(arr) - k:
            cur = cur + arr[k + i] - arr[i]
            res = max(res, cur)
            i += 1
        return res
    
