class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.updateTree(i, nums[i])

    def updateTree(self, i, delta):
        i += 1
        while i < len(self.sum):
            self.sum[i] += delta
            i += i & (-i)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.updateTree(index, delta)

    def sumTree(self, i):
        total = 0
        i += 1
        while i > 0:
            total += self.sum[i]
            i -= i & (-i)
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self.sumTree(right) - self.sumTree(left - 1)

