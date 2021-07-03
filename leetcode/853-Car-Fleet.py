class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(target - p) / s for p, s in sorted(zip(position, speed))[::-1]]
        cur = res = 0
        for time in arr:
            if time > cur:
                res += 1
                cur = time
        return res
