class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not nums: return 0
        cnt, prev = 0, nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                cnt += prev - nums[i] + 1
                prev = prev + 1
            else:
                prev = nums[i]
        return cnt
