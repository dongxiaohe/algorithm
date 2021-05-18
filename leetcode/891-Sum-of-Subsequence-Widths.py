class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        def backtrack(nums, start, arr, res):
            if arr: res.append(arr)
            if start == len(nums): return
            for i in range(start, len(nums)):
                backtrack(nums, i + 1, arr + [nums[i]], res)
        res = []
        cnt = 0
        backtrack(nums, 0, [], res)
        for each in res:
            cnt += max(each) - min(each)
        return cnt
