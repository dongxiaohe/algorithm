class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        kv = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in kv:
                if stack and stack[-1] == kv[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
