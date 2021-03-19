class FenwickTree:
    def __init__(self, size):
        self.counter = [0] * (size + 1)
    def update(self, index):
        index += 1
        while index < len(self.counter):
            self.counter[index] += 1
            index += index & (-index)
    def query(self, index):
        _sum = 0
        while index > 0:
            _sum += self.counter[index]
            index -= index & (-index)
        return _sum
class Solution(object):
    def countSmaller(self, nums):
        kv = {v : i for i, v in enumerate(sorted(set(nums)))}
        tree = FenwickTree(len(kv))
        res = []
        for val in nums[::-1]:
            res.append(tree.query(kv[val]))
            tree.update(kv[val])
        return res[::-1]
