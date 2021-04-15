class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evenArr, oddArr = [], []
        for a in A:
            if a & 1 == 1:
                oddArr.append(a)
            else:
                evenArr.append(a)
        return evenArr + oddArr
