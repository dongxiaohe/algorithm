class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(arr):
            st = set(arr)
            if len(st) != len(arr): return len(st) == 1
            mn, mx = min(arr), max(arr)
            if (mx - mn) % (len(arr) - 1) != 0: return False # make sure float value cast to integer
            diff = (mx - mn) // (len(arr) - 1) 
            for step in range(mn, mx, diff):
                if step not in st: return False
            return True
        return [isArithmetic(nums[start: stop + 1]) for start, stop in zip(l, r)]

