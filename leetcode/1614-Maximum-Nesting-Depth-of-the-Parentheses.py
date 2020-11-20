class Solution(object):
    def maxDepth(self, s):
        mx, cur = 0, 0
        for e in s:
            if e == '(':
                cur += 1
            elif e == ')':
                cur -= 1
            mx = max(mx, cur)
        return mx
