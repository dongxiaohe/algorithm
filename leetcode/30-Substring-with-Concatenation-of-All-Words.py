class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        wordCounter = collections.Counter(words)
        wordCount, wordLen, result = len(words), len(words[0]), []
        for i in range(len(s) - wordCount * wordLen + 1):
            seen = collections.defaultdict(int)
            for j in range(i, i + wordLen * wordCount, wordLen):
                curWord = s[j: j + wordLen]
                if curWord in wordCounter:
                    seen[curWord] += 1
                    if seen[curWord] > wordCounter[curWord]: break
                else: break
            if wordCounter == seen:
                result.append(i)
        return result
