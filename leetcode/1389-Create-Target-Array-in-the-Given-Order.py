class Solution:
    # Note this is a still N ^ 2 solution, there is n * logN solution by using merge sort
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res
