class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        kv = defaultdict(list)
        for i in range(len(s1)):
            kv[s1[i]].append(i)
        _start, seen, res = -1, -1, []
        while True:
            start, cur, size = -1, seen, 0
            for i in range(len(s2)):
                ch = s2[i]
                if ch in kv:
                    index = bisect.bisect_right(kv[ch], cur)
                    if index >= len(kv[ch]): 
                        return "" if not res else min(res, key = len) 
                    cur = kv[ch][index]
                    if start == -1: 
                        start = cur
                else:
                    return "" if not res else min(res, key = len)
            seen = start
            res.append(s1[start : cur + 1])
