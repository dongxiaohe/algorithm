class Solution:
    def numWays(self, s: str) -> int:
        def _backtrack(s, start, arr, result):
            if start == len(s):
                if 3 == len(arr) and Counter(arr[0])["1"] == Counter(arr[1])["1"] == Counter(arr[2])["1"]:
                    result["count"] += 1
            for i in range(start, len(s)):
                _backtrack(s, i + 1, arr + [s[start :i + 1]], result)
        result = {}
        result["count"] = 0
        _backtrack(s, 0, [], result)
        return result["count"]
    
