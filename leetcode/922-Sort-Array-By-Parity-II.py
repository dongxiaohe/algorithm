class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds, even = [], []
        for i in range(len(nums)):
            if i & 1 != (nums[i] & 1):
                if i & 1 == 0:
                    even.append(i)
                else:
                    odds.append(i)
        for i in range(len(odds)):
            nums[odds[i]], nums[even[i]] = nums[even[i]], nums[odds[i]]
        return nums

