class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0 for _ in range(n + 1)]
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
        for i in range(1, n + 1):
            freq[i] += freq[i - 1]
        res = 0
        for x, y in zip(sorted(freq[:-1]), sorted(nums)):
            res += x * y
        return res % (10 ** 9 + 7)
