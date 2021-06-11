class NumArray(object):

    def __init__(self, nums):
        self.sum = [0] * len(nums)
        self.sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.sum[i] = self.sum[i - 1] + nums[i]

    def sumRange(self, left, right):
        if left != 0:
            return self.sum[right] - self.sum[left - 1]
        return self.sum[right]

