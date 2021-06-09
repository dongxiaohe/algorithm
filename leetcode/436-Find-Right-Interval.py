class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = []
        for i in range(len(intervals)):
            start, _ = intervals[i]
            bisect.insort_left(arr, [start, i])
        res = []
        for start, end in intervals:
            position = bisect.bisect_right(arr, [end, float("-inf")])
            if position == len(arr):
                res.append(-1)
            else:
                res.append(arr[position][1])
        return res
