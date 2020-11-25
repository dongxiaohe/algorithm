class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        left, n, res = 0, len(s), 0
        while left < n:
            right = left + 1
            while right < n and s[right] == s[left]:
                right += 1
            if right - left > 1:
                total = cost[left: right]
                res += sum(total) - max(total)
            left = right
        return res

