class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        _max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], _max = _max, max(_max, arr[i])
        return arr
