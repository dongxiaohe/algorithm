class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = coordinates
        return ord(x) & 1 ^ (int(y) & 1)
