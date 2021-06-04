class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isValid(nums, target, m):
            cnt, acc = 1, 0
            for num in nums:
                acc += num
                if acc > target:
                    cnt += 1
                    acc = num
                if cnt > m: return False
            return True
        _max, _sum = float("-inf"), 0
        for num in nums:
            _max = max(_max, num)
            _sum += num
        l, r = _max, _sum
        if m == 1:
            return _sum
        while l < r:
            mid = l + (r - l >> 1)
            if isValid(nums, mid, m):
                r = mid
            else:
                l = mid + 1
        return l
