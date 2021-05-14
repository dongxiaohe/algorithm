class Solution:
    def fib(self, n: int) -> int:
        def _fib(n, mem):
            if n in mem: return mem[n]
            res = None
            if n == 0:
                res = 0
            elif n == 1:
                res = 1
            else:
                res = _fib(n - 1, mem) + _fib(n - 2, mem)
            mem[n] = res
            return res
        return _fib(n, {})

