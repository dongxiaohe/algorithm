class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            if 9 < val < 100 or 999 < val < 10000 or val == 100000:
                res += 1
        return res
