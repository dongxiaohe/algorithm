class Solution:
    def isArithmetic(self, arr):
        st = set(arr)
        if len(st) != len(arr): return len(st) == 1
        mn, mx = min(arr), max(arr)
        if (mx - mn) % (len(arr) - 1) != 0: return False # make sure float value cast to integer
        diff = (mx - mn) // (len(arr) - 1) 
        for step in range(mn, mx, diff):
            if step not in st: return False
        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            result.append(self.isArithmetic(nums[l[i]: r[i] + 1]))
        return result
