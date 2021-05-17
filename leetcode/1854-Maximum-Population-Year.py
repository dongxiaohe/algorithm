class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        total = 2050 - 1950 + 1
        years, res = [0] * total, 0
        for x, y in logs:
            years[x - 1950] += 1
            years[y - 1950] -= 1
        for i in range(1, total):
            years[i] += years[i - 1]
            res = i if years[i] > years[res] else res
        return res + 1950
