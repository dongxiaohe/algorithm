class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        res = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res
