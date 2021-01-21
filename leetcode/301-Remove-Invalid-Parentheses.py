class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for ch in s:
            if ch == "(": left += 1
            elif ch == ")":
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else 0
        def _backtrack(s, i, left, right, opened, acc, result):
            if i == len(s):
                if left == right == opened == 0:
                    result[acc] = 1
                return
            if (s[i] == "(" and left > 0) or (s[i] == ")" and right > 0):
                _backtrack(s, i + 1, left - (s[i] == "("), right - (s[i] == ")"), opened, acc, result)
            if s[i] != "(" and s[i] != ")":
                _backtrack(s, i + 1, left, right, opened, acc + s[i], result)
            elif s[i] == "(":
                _backtrack(s, i + 1, left, right, opened + 1, acc + s[i], result)
            elif s[i] == ")" and opened > 0:
                _backtrack(s, i + 1, left, right, opened - 1, acc + s[i], result)
        result = {}
        _backtrack(s, 0, left, right, 0, "", result)
        return list(result.keys())

