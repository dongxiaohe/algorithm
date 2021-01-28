class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        start, steps, maxSteps, nextMaxSteps = 0, 0, 0, 0
        while True:
            steps += 1
            for i in range(start, maxSteps + 1):
                nextMaxSteps = max(nextMaxSteps, nums[i] + i)
                if nextMaxSteps >= len(nums) - 1: return steps
            start = maxSteps + 1
            maxSteps = nextMaxSteps
        return steps

