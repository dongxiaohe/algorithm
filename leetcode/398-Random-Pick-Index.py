class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        reservoir = -1
        cnt = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                cnt += 1
                index = random.randint(0, cnt - 1)
                if index == 0:
                    reservoir = i
        return reservoir
