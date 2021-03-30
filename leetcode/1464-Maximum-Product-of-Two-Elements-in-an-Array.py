class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max1 = _max2 = 0
        for val in nums:
            if val > _max1:
                _max2 = _max1
                _max1 = val
            elif val > _max2:
                _max2 = val
        return (_max1 - 1) * (_max2 - 1)
