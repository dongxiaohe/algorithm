class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        _sum = 0
        kv = {}
        kv[0] = -1
        for i, v in enumerate(nums):
            _sum += v
            if k != 0: _sum %= k
            if _sum in kv:
                if i - kv[_sum] > 1: return True
            else:kv[_sum] = i
        return False

