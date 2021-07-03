class Solution:
    def modifyString(self, s: str) -> str:
        previous, forward, res = "", "", []
        for i in range(len(s)):
            cur = s[i]
            if cur == "?":
                if i - 1 >= 0:
                    previous = res[i - 1]
                if i + 1 < len(s):
                    forward = s[i + 1]
                for ch in string.ascii_lowercase:
                    if ch != previous and ch != forward:
                        cur = ch
            res.append(cur)
        return "".join(res)
