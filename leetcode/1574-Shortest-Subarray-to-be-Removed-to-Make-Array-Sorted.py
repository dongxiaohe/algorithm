class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        res = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < n and arr[right] < arr[left]: # this is the key for diff [1,3,7,6,5] [1,3,7,4,5]
                right += 1
            res = min(res, right - left - 1)
            left += 1
        return res

