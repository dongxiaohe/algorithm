class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        countOne = 0
        for val in arr:
            if val == 1: countOne += 1
        if countOne == 0:
            return [0, len(arr) - 1]
        if countOne % 3 != 0:
            return [-1, -1]
        k, i = countOne // 3, 0
        start, mid, end = 0, 0, 0
        countStart, countMid, countEnd = 1, k + 1, 2 * k + 1
        count = 0
        while i < len(arr):
            if arr[i] == 1:
                count += 1
                if count == countStart:
                    start = i
                elif count == countMid:
                    mid = i
                elif count == countEnd:
                    end = i
                    break
            i += 1
        while end < len(arr) and arr[start] == arr[mid] == arr[end]:
            start += 1
            mid += 1
            end += 1
        if end == len(arr):
            return [start - 1, mid]
        return [-1, -1]
        

