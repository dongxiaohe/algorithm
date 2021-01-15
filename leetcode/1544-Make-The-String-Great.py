class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1].lower() == ch.lower() and stack[-1] != ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
