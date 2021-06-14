class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s: return 0
        pre, cur, tmp, res = 1, 0, s[0], 0
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                if cur > 0:
                    res += min(pre, cur)
                    pre = cur
                cur = 1
            else:
                if cur > 0: cur += 1
                else: pre += 1
        res += min(pre, cur)
        return res
