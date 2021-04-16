class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        kv, cnt, duplicates = set(), 0, set()
        for val in nums:
            if val not in kv:
                kv.add(val)
                cnt += val
            else:
                duplicates.add(val)
        return cnt - sum(duplicates)
