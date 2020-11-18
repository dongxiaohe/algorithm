class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        result = [keysPressed[0], releaseTimes[0]]
        for i in range(n - 1):
            newDiff = releaseTimes[i + 1] - releaseTimes[i]
            if newDiff >= result[1]:
                if newDiff == result[1]: 
                    result = [max(result[0], keysPressed[i + 1]), newDiff]
                else:
                    result = [keysPressed[i + 1], newDiff]
        return result[0]

