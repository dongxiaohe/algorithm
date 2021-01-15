from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        leftKv, rightKv, res = {}, Counter(s), 0
        for i in range(len(s)):
            if s[i] not in leftKv:
                leftKv[s[i]] = 1
            else:
                leftKv[s[i]] += 1
            rightKv[s[i]] -= 1
            if rightKv[s[i]] == 0:
                del rightKv[s[i]]
            if len(leftKv.keys()) == len(rightKv.keys()):
                res += 1
        return res
