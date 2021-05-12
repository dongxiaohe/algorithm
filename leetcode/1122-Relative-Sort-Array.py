class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt, ref = collections.Counter(arr1), collections.Counter(arr2)
        res = []
        for val in arr2:
            while cnt[val] > 0:
                res.append(val)
                cnt[val] -= 1
        arr = []
        for val in arr1:
            if val not in ref:
                arr.append(val)
        return res + sorted(arr)
