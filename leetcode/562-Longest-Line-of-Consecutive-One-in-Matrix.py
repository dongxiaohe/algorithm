class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat: return 0
        def score(line):
            return max(len(list(v)) if k else 0 for k, v in itertools.groupby(line))
        groups = collections.defaultdict(list)
        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                groups[0, r].append(val)
                groups[1, c].append(val)
                groups[2, r + c].append(val)
                groups[3, r - c].append(val)
        return max(map(score, groups.itervalues()))
