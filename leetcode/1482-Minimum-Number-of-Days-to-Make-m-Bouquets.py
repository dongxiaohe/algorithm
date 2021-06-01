class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isValid(arr, m, k):
            i, n, cnt = 0, len(arr), 0
            while i < n:
                found = False
                j = i
                if arr[i]:
                    j = i
                    while j < n and arr[j]:
                        if j - i + 1 == k:
                            cnt += 1
                            found = True
                            break
                        j += 1
                if not found:
                    i += 1
                else:
                    i = j + 1
            return cnt >= m
        if m * k > len(bloomDay): return -1
        _min = min(bloomDay)
        while True:
            arr = list(map(lambda x: x <= _min, bloomDay))
            if isValid(arr, m, k): return _min
            _min += 1

