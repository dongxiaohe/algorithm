class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                j = len(arr) - 1
                while j > i + 1:
                    arr[j] = arr[j - 1]
                    j -= 1
                if i < len(arr) - 1:
                    arr[i + 1] = 0
                i += 2
            else:
                i += 1

