class Solution:
    def sortSentence(self, s: str) -> str:
        words, kv = s.split(" "), {}
        for word in words:
            number = int(word[-1])
            kv[number] = word[:-1]
        k, res = 1, []
        while k <= len(words):
            res.append(kv[k])
            k += 1
        return " ".join(res)
