class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    nextWord = word[:i] + ch + word[i + 1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append([nextWord, length + 1])
        return 0
