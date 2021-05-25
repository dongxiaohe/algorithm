class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        kv = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first, second = 0, 0
        for i in range(len(s)):
            if i < (len(s) >> 1):
                first += 1 if s[i] in kv else 0
            else:
                second += 1 if s[i] in kv else 0
        return first == second
