class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        kv, half, cnt = "aeiouAEIOU", len(s) >> 1, 0
        for i in range(len(s)):
            if s[i] in kv:
                cnt += 1 if i < half else -1
        return  cnt == 0
