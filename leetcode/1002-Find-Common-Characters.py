class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        kv, res = {}, []
        for i in range(len(A)):
            kv[i] = collections.Counter(A[i])
        for ch in A[0]:
            found = True
            for i in range(1, len(A)):
                if ch in kv[i] and kv[i][ch] > 0:
                    kv[i][ch] -= 1
                else:
                    found = False
                    break
            if found: res.append(ch)
        return res
