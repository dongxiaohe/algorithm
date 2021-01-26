class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        startQueue, endQueue, length = collections.deque([beginWord]), collections.deque([endWord]), 1
        while startQueue and endQueue:
            if len(startQueue) > len(endQueue):
                startQueue, endQueue = endQueue, startQueue
            i, size = 0, len(startQueue)
            while i < size:
                word = startQueue.popleft()
                for j in range(len(word)):
                    for ch in string.ascii_lowercase:
                        nextWord = word[:j] + ch + word[j + 1:]
                        if nextWord in endQueue:
                            return length + 1
                        if nextWord in wordSet:
                            wordSet.remove(nextWord)
                            startQueue.append(nextWord)
                i += 1
            length += 1
        return 0
