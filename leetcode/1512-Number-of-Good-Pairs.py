class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums).values()
        res = 0
        for k in counter:
            res += k * (k - 1) // 2
        return res
