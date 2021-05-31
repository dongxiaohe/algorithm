class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros, ones, zero, maxZeros, maxOnes = 0, 0, None, 0, 0
        for c in s:
            if c == "0":
                if zero == True:
                    zeros += 1
                else:
                    zero = True
                    zeros = 1
                maxZeros = max(maxZeros, zeros)
            else:
                if zero == False:
                    ones += 1
                else:
                    zero = False
                    ones = 1
                maxOnes = max(maxOnes, ones)
        return maxOnes > maxZeros
