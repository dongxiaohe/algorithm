# [1, 1, 1, 1, 1]
# loop/stats      sum          map          res
# 1                1        (0, 0) (1, 0)    0
# 2                2        + (2, 1)         1
# 3                3        + (3, 1)         1
# 4                4        + (4, 2)         2
# 5                5        + (5, 2)         2
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res, kv, _sum = 0, {}, 0
        kv[0] = 0
        for val in nums:
            _sum += val
            if _sum - target in kv:
                res = max(res, kv[_sum - target] + 1)
            kv[_sum] = res
        return res
