class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        res = [0] * 2 * n
        for i in range(n):
            res[i + n] = res[i] = nums[i]
        return res
