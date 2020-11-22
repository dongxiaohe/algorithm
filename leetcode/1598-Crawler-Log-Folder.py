class Solution(object):
    def minOperations(self, logs):
        mn = 0
        for log in logs:
            if log == '../':
                mn = max(0, mn - 1)
            elif log != './':
                mn += 1
        return mn
