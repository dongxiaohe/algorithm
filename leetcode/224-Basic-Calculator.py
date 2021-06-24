class Solution:
    def calculate(self, s: str) -> int:
        stack, number, sign, result = [], 0, 1, 0
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == "+":
                result += sign * number
                number = 0
                sign = 1
            elif ch == "-":
                result += sign * number
                number = 0
                sign = -1
            elif ch == ")":
                result += sign * number
                result *= stack.pop()
                result += stack.pop()
                number = 0
        if number:
            result += sign * number
        return result
