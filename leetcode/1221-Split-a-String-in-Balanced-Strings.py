class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right, cnt = 0, 0, 0
        for ch in s:
            if ch == "L":
                left += 1
            else:
                right += 1
            if left == right:
                cnt += 1
        return cnt
