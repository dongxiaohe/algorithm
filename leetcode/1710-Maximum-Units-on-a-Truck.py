class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        total = 0
        sortedBoxTypes = sorted(boxTypes, key = lambda x: -x[1])
        i, num = 0, 0
        while num < truckSize and i < len(sortedBoxTypes):
            if truckSize - sortedBoxTypes[i][0] - num >= 0:
                total += sortedBoxTypes[i][1] * sortedBoxTypes[i][0]
                num += sortedBoxTypes[i][0]
            else:
                return total + (truckSize - num) * sortedBoxTypes[i][1]
            i += 1
        return total
