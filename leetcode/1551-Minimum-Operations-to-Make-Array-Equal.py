class Solution:
    def minOperations(self, n: int) -> int:
        h = n // 2
        if n % 2 == 1:
            return h * (h + 1)
        return h * h
