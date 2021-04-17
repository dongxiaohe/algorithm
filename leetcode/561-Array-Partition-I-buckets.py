class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        res = 0
        lower, higher, minFound = -10 ** 4, 10 ** 4, False
        while lower <= higher:
            if counter[lower] > 0:
                if not minFound:
                    res += lower
                    minFound = True
                else:
                    minFound = False
                counter[lower] -= 1
            if counter[lower] == 0: lower += 1
        return res
