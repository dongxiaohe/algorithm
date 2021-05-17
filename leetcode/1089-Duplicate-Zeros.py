class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = arr.count(0)
        for i in range(len(arr) - 1, -1, -1):
            if i + zeros < len(arr):
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < len(arr):
                    arr[i + zeros] = 0
