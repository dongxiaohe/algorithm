class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l, r = 0, 0 
        while l < len(arr):
            if arr[l] % 2 == 1:
                r = l + 1
                while r < len(arr):
                    if arr[r] % 2 == 0:
                        l = r 
                        break
                    if r - l == 2:    
                        return True
                    r += 1
            l += 1
        return False
