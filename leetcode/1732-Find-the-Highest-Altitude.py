class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        _max, tmp = 0, 0
        for val in gain:
            tmp += val
            _max = max(tmp, _max)
        return _max
