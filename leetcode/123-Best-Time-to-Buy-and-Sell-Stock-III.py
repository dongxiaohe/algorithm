class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2, sell1, sell2 = float("inf"), float("inf"), 0, 0
        for each in prices:
            buy1 = min(buy1, each)
            sell1 = max(sell1, each - buy1)
            buy2 = min(buy2, each - sell1)
            sell2 = max(sell2, each - buy2)
        return sell2
