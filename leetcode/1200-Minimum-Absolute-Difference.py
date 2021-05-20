class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff, res = float("inf"), []
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            if diff < minDiff:
                res = []
                minDiff = diff
                res.append([arr[i - 1], arr[i]])
            elif diff == minDiff:
                res.append([arr[i - 1], arr[i]])
        return res
