class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def getSoilders(arr) -> int:
            l, r = 0, len(arr)
            while l < r:
                m = l + (r - l >> 1)
                if arr[m] == 0:
                    r = m
                else:
                    l = m + 1
            return l
        soildersArr = []
        for i in range(len(mat)):
            soildersArr.append([getSoilders(mat[i]), i])
        return list(map(lambda x: x[1], sorted(soildersArr)))[:k]
