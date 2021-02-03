class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j, iMatch, jWildcardAfter, lenS, lenP = 0, 0, 0, -1, len(s), len(p)
        while i < lenS:
            if j < lenP and (p[j] == "?" or s[i] == p[j]):
                i += 1
                j += 1
            elif j < lenP and p[j] == "*":
                #at start, iMatch point to first s and iWildcard match to the character after *
                jWildcardAfter = j
                j += 1
                iMatch = i
            elif jWildcardAfter != -1:
                # if not match, reset j to pointer after * and i after pointer iMatch + 1
                j = jWildcardAfter + 1
                iMatch += 1
                i = iMatch
            else: return False
        while j < lenP and p[j] == "*": j += 1
        return j == lenP

