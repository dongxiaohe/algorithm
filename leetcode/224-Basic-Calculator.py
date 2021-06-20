class Solution:
    def calculate(self, s: str) -> int:
        op, prev, cur = 1, 0, ""
        for i in range(len(s)):
            if s[i] == "+":
                op = 1
            elif s[i] == "-":
                op = -1
            elif s[i] == "(" or s[i] == ")":
                continue
            else:
                if s[i] != " " and i + 1 < len(s) and not s[i + 1].isdigit():
                   
                    prev += int((cur + s[i]).strip() ) * op
                    cur = ""
                else:
                    cur += s[i]
        if cur.strip().isdigit():
            return prev + int(cur.strip()) * op
        return prev
    
