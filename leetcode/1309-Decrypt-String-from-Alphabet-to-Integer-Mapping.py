class Solution:
    def freqAlphabets(self, s: str) -> str:
        def alpha(num):
            return chr(int(num) + ord('a') - 1)
        i, res = 0, []
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                res.append(alpha(s[i: i + 2]))
                i += 3
            else:
                res.append(alpha(s[i]))
                i += 1
        return "".join(res)
