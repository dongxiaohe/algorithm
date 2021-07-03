class Solution:
    def reformat(self, s: str) -> str:
        digits, chs = [], []
        for ch in s:
            if ch.isdigit(): digits.append(ch)
            else: chs.append(ch)
        if abs(len(digits) - len(chs)) > 1: return ""
        res = []
        if len(digits) > len(chs): 
            chs.append("")
            for digit, ch in zip(digits, chs):
                res.append(digit)
                res.append(ch)
        else:
            digits.append("")
            for digit, ch in zip(digits, chs):
                res.append(ch)
                res.append(digit)
        return "".join(res)
