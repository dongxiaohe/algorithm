class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        deficit, acc = 0, 0
        for each in nums:
            acc += each
            deficit = min(deficit, acc)
        return abs(deficit) + 1
