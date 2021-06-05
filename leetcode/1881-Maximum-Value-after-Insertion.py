class Solution:
    def maxValue(self, n: str, x: int) -> str:
        for i in range(len(n)):
            if [n[i] < str(x), n[i] > str(x)][n[0] == "-"]:
                return n[:i] + str(x) + n[i:]
        return n + str(x)
