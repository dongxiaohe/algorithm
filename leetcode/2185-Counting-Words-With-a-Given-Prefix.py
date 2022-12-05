class Solution(object):
    def prefixCount(self, words, pref):
        cnt = 0
        for word in words:
            if word[:len(pref)] == pref:
                cnt += 1
        return cnt
