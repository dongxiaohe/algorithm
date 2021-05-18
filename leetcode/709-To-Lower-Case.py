class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for ch in str:
            if 65 <= ord(ch) <= 91:
                res.append(chr(ord(ch) + 32))
            else:
                res.append(ch)
        return "".join(res)
