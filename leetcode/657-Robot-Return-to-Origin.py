class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l, r, u, d = 0, 0, 0, 0
        for move in moves:
            if move == "U": u += 1
            if move == "D": d += 1
            if move == "L": l += 1
            if move == "R": r += 1
        return u == d and l == r
