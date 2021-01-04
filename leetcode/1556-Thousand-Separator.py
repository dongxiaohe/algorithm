class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        start = len(s)
        deque = collections.deque()
        while start >= 1:
            i = 0 if start - 3 < 0 else start - 3
            deque.append(s[i:start])
            start -= 3
        result = ""
        while deque:
            result = deque.popleft() + result
            if len(deque) > 0:
                result = "." + result
        return result

    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        s = s[::-1]
        # 1. t = "1234567" t[0:7] == t[0:100]
        # 2. s[i: i + 3] for i in range(0, len(s), 3) return a generator
        result = ".".join(s[i:i + 3] for i in range(0, len(s), 3))
        return result[::-1]
