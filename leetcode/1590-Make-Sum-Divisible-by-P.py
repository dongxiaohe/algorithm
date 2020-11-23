class Solution(object):
    def minSubarray(self, nums, p):
        need = sum(nums) % p
        dp = {0: -1}
        cur = 0
        res = len(nums)
        for i, a, in enumerate(nums):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                res = min(res, i - dp[(cur - need) % p])
        return res if res < len(nums) else -1

