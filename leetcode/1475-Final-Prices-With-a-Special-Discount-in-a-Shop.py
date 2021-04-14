class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices):
                if prices[j] <= prices[i]: 
                    res.append(prices[i] - prices[j])
                    break
                j += 1
            if len(res) == i:
                res.append(prices[i])
        return res
