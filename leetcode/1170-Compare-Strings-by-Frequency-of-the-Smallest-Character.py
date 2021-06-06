class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def getFrequency(word):
            kv = Counter(word)
            for i in range(26):
                ch = chr(i + 97)
                if kv[ch] > 0: return kv[ch]
        qCounter = list(map(lambda x: getFrequency(x), queries))
        wordCounter = list(map(lambda x: getFrequency(x), words))
        res = []
        for each in qCounter:
            cnt = 0
            for word in wordCounter:
                if word > each: cnt += 1
            res.append(cnt)
        return res
