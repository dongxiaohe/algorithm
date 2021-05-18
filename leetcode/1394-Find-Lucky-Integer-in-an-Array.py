class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        k = len(arr)
        while k > 0:
            if counter[k] == k:
                return k
            k -= 1
        return -1
