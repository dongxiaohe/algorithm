class Solution:
    def getCollisionTimes(self, A: List[List[int]]) -> List[float]:
        """
Your input
[[3,4],[5,4],[6,3],[9,1]]
Output
[2.00000,1.00000,1.50000,-1.00000] , compare [3, 4] with [6, 3] and [9. 1] 
(A[stack[-1]][0] - p) / (s - A[stack[-1]][1]) >= res[stack[-1]] > 0) is classic
Expected
[2.00000,1.00000,1.50000,-1.00000]
        """
        stack, m = [], len(A)
        res = [-1] * m
        for i in range(m - 1, -1, -1):
            p, s = A[i]
            while stack and (s <= A[stack[-1]][1] or (A[stack[-1]][0] - p) / (s - A[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (A[stack[-1]][0] - p) / (s - A[stack[-1]][1])
            stack.append(i)
        return res
