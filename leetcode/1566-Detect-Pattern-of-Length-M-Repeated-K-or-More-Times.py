class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        cnt = 0
        for i in range(len(arr) - m):
            if arr[i] != arr[i + m]:
                cnt = 0
            cnt += arr[i] == arr[i + m]
            if cnt == (k - 1) * m:
                return True
        return False
