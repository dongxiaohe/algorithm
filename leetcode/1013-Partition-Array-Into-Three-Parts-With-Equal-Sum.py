class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        _sum = sum(arr) 
        if _sum % 3 != 0: return False
        average, tmp, count = _sum / 3, 0, 0
        for number in arr:
            tmp += number
            if average == tmp:
                tmp = 0
                count += 1
        return count >= 3
