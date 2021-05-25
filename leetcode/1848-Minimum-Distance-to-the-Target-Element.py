class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        distance, res = float("inf"), -1
        l, r, turn = start, start + 1, True
        while l >= 0 or r < len(nums):
            if l >= 0 and nums[l] == target:
                return start - l
                l -= 1
            if r < len(nums) and nums[r] == target:
                return r - start
            r += 1
            l -= 1

