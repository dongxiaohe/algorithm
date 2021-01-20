class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack, res = [], 0
        for ch in S:
            if ch == "(":
                stack.append(res)
                res = 0
            else:
                res += stack.pop() + max(res, 1)
        return res
