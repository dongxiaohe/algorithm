class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        total, num = 0, 0
        hqBoxTypes = list(map(lambda x: (-x[1], x[0]), boxTypes))
        heapq.heapify(hqBoxTypes)
        while num < truckSize and hqBoxTypes:
            size, cnt = heapq.heappop(hqBoxTypes)
            if truckSize - num - cnt >= 0:
                total += -size * cnt
                num += cnt
            else:
                return total + (truckSize - num) * -size
        return total
