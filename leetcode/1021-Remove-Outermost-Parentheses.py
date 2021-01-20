class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opened = "", 0 
        for ch in S:
            if ch == "(" and opened > 0: res += ch
            elif ch == ")" and opened > 1: res += ch
            opened += 1 if ch == "(" else -1
        return res
            
