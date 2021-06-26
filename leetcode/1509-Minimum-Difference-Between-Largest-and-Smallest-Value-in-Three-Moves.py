class Solution:
    def minDifference(self, nums: List[int]) -> int:
        top4 = heapq.nlargest(4, nums)[::-1]
        bot4 = heapq.nsmallest(4, nums)
        """
        1,2,3,4,5,6,7,8,9,10
        [1, 7],
        [2, 8],
        [3, 9],
        [4, 10]
        so we inverse top4 or bot4
        """
        return min([x - y for x,y in zip(top4, bot4)])
