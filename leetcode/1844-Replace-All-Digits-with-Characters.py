class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(0, len(s), 2):
            res.append(s[i])
            if i + 1 < len(s):
                nextCh = chr(ord(s[i]) + int(s[i + 1]))
                res.append(nextCh)
        return "".join(res)
