class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        kv = collections.Counter(chars)
        cnt = 0
        for word in words:
            wordCnt = collections.Counter(word)
            matched = True
            for key in wordCnt:
                if wordCnt[key] > kv[key]:
                    matched = False
                    break
            if matched: cnt += len(word)
        return cnt
