class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack, res = [], 0
        for ch in S:
            if ch == "(": stack.append(ch)
            elif ch == ")": 
                if len(stack) > 0:
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)
