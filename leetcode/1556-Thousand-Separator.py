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
