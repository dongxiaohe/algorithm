class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res, _sum = [], 0
        for each in nums:
            res.append(each + _sum)
            _sum += each
        return res
