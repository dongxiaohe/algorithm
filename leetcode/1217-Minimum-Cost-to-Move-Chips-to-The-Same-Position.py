class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for val in position:
            if val & 1 == 1:
                odd += 1
            else:
                even += 1
        return min(odd, even)
