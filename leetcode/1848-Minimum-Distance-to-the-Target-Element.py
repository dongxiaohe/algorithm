class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        distance, res = float("inf"), -1
        l, r, turn = start, start + 1, True
        while l >= 0 or r < len(nums):
            if abs(l - start) <= abs(r - start):
                if l >= 0 and nums[l] == target:
                    return abs(l - start)
                l -= 1
            else:
                if r < len(nums) and nums[r] == target:
                    return abs(r - start)
                r += 1
