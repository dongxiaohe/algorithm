class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = collections.Counter(heights)
        cnt, lower, upper, i = 0, 0, 100, 0
        while lower <= upper:
            if counter[lower] > 0:
                if heights[i] != lower: cnt += 1
                counter[lower] -= 1
                i += 1
            if counter[lower] == 0:
                lower += 1
        return cnt
        
