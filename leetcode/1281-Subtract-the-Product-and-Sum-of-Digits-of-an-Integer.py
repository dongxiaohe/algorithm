class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _sum, product = 0, 1
        while n > 0:
            _sum += n % 10
            product *= n % 10
            n //= 10
        return product - _sum

