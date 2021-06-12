class Solution(object):
    def decodeString(self, s):
        a, b, stack = "", "", []
        res = []
        for ch in s:
            if ch.isdigit():
                a += ch
            elif ch == "[":
                stack.append(a)
                stack.append(b)
                a, b = "", ""
            elif ch == "]":
                _str = stack.pop()
                _number = int(stack.pop())
                b = _str + b * _number
                if not stack:
                    res.append(b)
                    b = ""
            else:
                b += ch
        return "".join(res) + b
