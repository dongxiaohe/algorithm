class Solution:
    def minInsertions(self, s: str) -> int:
        res, right = 0, 0
        # What cases we have to add parenthesis
        # 1. There is no outstanding ( but we add )
        # 2. Odd number ) are required but we add (
        # 3. The final result is the number of ) required + (, ) are already added
        for ch in s:
            if ch == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1 # We have to add a left parenthesis
            else:
                if right % 2:
                    right -= 1
                    res += 1 # We have to add a right parenthesis
                right += 2
        return right + res
