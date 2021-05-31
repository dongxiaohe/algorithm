class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, cnt = 1, 1
        for val in arr: 
            if i != val:
                while i < val:
                    if cnt == k:
                        return i
                    i += 1
                    cnt += 1
            i += 1
        return i + k - cnt

