class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            total = 0
            for each in nums:
                if each >> i & 1 == 1:
                    total += 1
            total %= 3
            if total == 1:
                res |= (total << i)
                if i == 31:
                    res -= 2 ** 32
        return res

