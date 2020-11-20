class Solution(object):
    def trimMean(self, arr):
        n = len(arr)
        k = n * 0.05
        return sum(sorted(arr)[k: -k]) / (n - 2k)

