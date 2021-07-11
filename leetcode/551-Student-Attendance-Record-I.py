class Solution:
    def checkRecord(self, s: str) -> bool:
        absentCounter = 0
        for i in range(len(s)):
            if s[i] == "A":
                absentCounter += 1
                if absentCounter == 2:
                    return False
            if s[i] == "L":
                j = i + 1
                while j < len(s) and s[j] == "L":
                    if j - i + 1 == 3:
                        return False
                    j += 1
        return True
