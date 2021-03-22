class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        return map(lambda candy: candy + extraCandies >= _max, candies)

