class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        left, right, n = 0, 0, len(arr)
        while left < n:
            right = left + 1 
            while right < n:
                if arr[left:right] in pieces:
                    if right == n: return True
                    left = right
                else:
                    right = right + 1
        return False
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        res = []
        for each in arr:
            res += mp.get(each, [])
        return res == arr

