class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        nums.sort()
        m = len(nums)
        diffs = float("inf")
        for x, y in [(0, 3), (1, 2), (2, 1), (3, 0)]:
            diffs = min(diffs, abs(nums[x] - nums[m - 1 - y]))
        return diffs
