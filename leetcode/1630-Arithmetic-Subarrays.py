class Solution:
    def isArithmetic(self, arr):
        sortedArr = sorted(arr)
        m = len(arr)
        if m <= 1: return False
        diff = sortedArr[1] - sortedArr[0]
        for i in range(len(arr) - 1):
            if sortedArr[i + 1] - sortedArr[i] != diff:
                return False
        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            result.append(self.isArithmetic(nums[l[i]: r[i] + 1]))
        return result
