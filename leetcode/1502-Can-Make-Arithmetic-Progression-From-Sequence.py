class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        _min1, _min2, kv = float("inf"), float("inf"), collections.Counter()
        for val in arr:
            kv[val] += 1
            if _min1 > val:
                _min2 = _min1
                _min1 = val
            elif _min2 > val:
                _min2 = val
        i, step = 0, _min2 - _min1
        while i < len(arr):
            if _min1 in kv and kv[_min1] > 0:
                kv[_min1] -= 1
            else:
                return False
            _min1 += step
            i += 1
        return True
