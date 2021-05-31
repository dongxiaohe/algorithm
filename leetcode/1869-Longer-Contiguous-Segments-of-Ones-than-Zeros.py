class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros, ones, maxZeros, maxOnes = 0, 0, 0, 0
        for c in s:
            if c == "0":
                zeros += 1
                maxZeros = max(maxZeros, zeros)
                ones = 0
            else:
                ones += 1
                maxOnes = max(maxOnes, ones)
                zeros = 0
        return maxOnes > maxZeros
