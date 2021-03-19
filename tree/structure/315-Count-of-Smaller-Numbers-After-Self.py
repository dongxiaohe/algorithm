class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, seen = [], []
        for val in nums[::-1]:
            position = bisect.bisect_left(seen, val)
            res.append(position)
            bisect.insort(seen, val)
        return res[::-1]

