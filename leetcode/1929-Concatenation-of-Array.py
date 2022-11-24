class Solution(object):
    def getConcatenation(self, nums):
        res = []
        n = len(nums)
        for i in range(n * 2):
            res.append(nums[i % n])
        return res
