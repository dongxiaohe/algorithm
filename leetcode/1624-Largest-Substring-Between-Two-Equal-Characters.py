class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        kv = collections.defaultdict(list)
        for i in range(len(s)):
            kv[s[i]].append(i)
        ans = -1
        for k, v in kv.items():
            if len(v) >= 2:
                ans = max(ans, v[-1] - v[0] - 1)
        return ans
