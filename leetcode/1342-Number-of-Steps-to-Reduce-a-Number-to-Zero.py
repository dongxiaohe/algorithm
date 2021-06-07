class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0: return 0
        cnt = 0
        while num != 0:
            cnt += 2 if num & 1 == 1 else 1
            num >>= 1
        return cnt - 1

