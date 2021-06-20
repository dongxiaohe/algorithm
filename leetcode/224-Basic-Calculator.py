class Solution:
    def calculate(self, s: str) -> int:
        def eval(s):
            op, prev, cur = 1, 0, ""
            for i in range(len(s)):
                if s[i] == "+":
                    op = 1
                elif s[i] == "-":
                    cnt = 1
                    j = i - 1
                    while j >= 0 and s[j] == "-":
                        cnt += 1
                        j -= 1
                    if cnt & 1 == 1:
                        op = -1
                    else:
                        op = 1          
                else:
                    if s[i] != " " and i + 1 < len(s) and not s[i + 1].isdigit():
                        prev += int((cur + s[i]).strip() ) * op
                        cur = ""
                    else:
                        cur += s[i]
            if cur.strip().isdigit():
                return prev + int(cur.strip()) * op
            return prev
        stack, cur, i = [], "", 0
        while i < len(s) or stack:
            if (i >= len(s) and stack) or s[i] == ")":
                tmp = []
                while stack:
                    ch = stack.pop()
                    if ch == "(":
                        break
                    tmp.append(ch)
                tmp = "".join(tmp[::-1]) + cur
                tmp = eval(tmp)
                cur = str(tmp)
            elif s[i] == "(":
                stack.append(cur)
                stack.append("(")
                cur = ""
            elif s[i] != " ": cur +=s[i]
            i += 1
        return eval(cur)
