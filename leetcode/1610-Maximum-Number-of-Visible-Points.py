class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        radians, extra = [], 0
        startX, startY = location
        for x, y in points:
            if x == startX and y == startY:
                extra += 1
                continue
            radians.append(math.atan2(x - startX, y - startY))
        radians.sort()
        radians += [x + 2 * math.pi for x in radians]
        ans, l, angle = 0, 0, math.pi * angle / 180
        for r in range(len(radians)):
            while radians[r] - radians[l] > angle:l += 1
            ans = max(ans, r - l + 1)
        return ans + extra
