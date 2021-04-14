class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, val in enumerate(prices):
            while stack and prices[stack[-1]] >= val:
                prices[stack.pop()] -= val
            stack.append(i)
        return prices

