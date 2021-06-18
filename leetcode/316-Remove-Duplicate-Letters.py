class Solution:
    res = None
    def removeDuplicateLetters(self, s: str) -> str:
        uniques = set(s)
        def backtrack(s, uniques, start, acc):
            if len(acc) > len(uniques): return
            if set(acc) == uniques:
                if not self.res: self.res = acc
                else:
                    self.res = min(acc, self.res)
                return
            for i in range(start, len(s)):
                backtrack(s, uniques, i + 1, acc + [s[i]])
        backtrack(s, uniques, 0, [])
        return "".join(self.res)
