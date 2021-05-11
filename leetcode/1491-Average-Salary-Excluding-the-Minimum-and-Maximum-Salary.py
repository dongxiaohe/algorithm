class Solution:
    def average(self, salary: List[int]) -> float:
        _min, _max, total = float("inf"), float("-inf"), 0
        for each in salary:
            total += each
            if each < _min: _min = each
            if each > _max: _max = each
        return (total - _min - _max) / (len(salary) - 2)

