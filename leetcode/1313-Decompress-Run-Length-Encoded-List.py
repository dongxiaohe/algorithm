class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            for _ in range(nums[i]):
                res.append(nums[i + 1])
        return res
