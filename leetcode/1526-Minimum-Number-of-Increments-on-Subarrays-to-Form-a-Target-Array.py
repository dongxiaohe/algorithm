class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        for val in target:
            res += max(0, val - pre)
            pre = val
        return res
