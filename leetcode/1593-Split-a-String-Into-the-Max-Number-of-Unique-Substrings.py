class Solution(object):
    def maxUniqueSplit(self, s):
        def _backtrack(s, seen):
            ans = 0
            for i in range(1, len(s) + 1):
                candidate = s[:i]
                if candidate not in seen:
                    seen.add(candidate)
                    ans = max(ans, 1 + _backtrack(s[i:], seen))
                    seen.remove(candidate)
            return ans
        seen = set()
        return _backtrack(s, seen)
