class Solution:
    def minWindow(self, s: str, t: str) -> str:
        state, missing = collections.defaultdict(int), len(t)
        for c in t: state[c] += 1
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= state[c] > 0
            state[c] -= 1
            if not missing:
                while i < j and state[s[i]] < 0:
                    state[s[i]] += 1
                    i += 1
                if not J or J - I > j - i:
                    I, J = i, j
        return s[I:J]
