class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = [0] * 101
        res = [0] * len(nums)
        for val in nums:
            counter[val] += 1
        for i in range(1, len(counter)):
            counter[i] += counter[i - 1]
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = 0
            else:
                res[i] = counter[nums[i] - 1]
        return res

