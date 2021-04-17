class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        kv = collections.Counter()
        for val in range(lowLimit, highLimit + 1):
            _sum = 0
            for digit in str(val):
                _sum += int(digit)
            kv[_sum] += 1
        return max(kv.values())
