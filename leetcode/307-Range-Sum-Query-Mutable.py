class FenwickTree:
    def __init__(self, nums):
        self.nums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])
    def update(self, i, delta):
        i += 1
        while i < len(self.nums):
            self.nums[i] += delta
            i += i & (-i)
    def query(self, i):
        i += 1
        _sum = 0
        while i > 0:
            _sum += self.nums[i]
            i -= i & (-i)
        return _sum
            
class NumArray:
    def __init__(self, nums: List[int]):
        self.fenwickTree = FenwickTree(nums)
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.fenwickTree.update(index, delta)
        self.nums[index] += delta

    def sumRange(self, left: int, right: int) -> int:
        return self.fenwickTree.query(right) - self.fenwickTree.query(left - 1)
