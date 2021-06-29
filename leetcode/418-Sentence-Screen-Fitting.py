class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        largestWord = max(sentence, key = lambda x: len(x))
        if len(largestWord) > cols: return 0
        allWords, start = " ".join(sentence) + " ", 0
        for i in range(rows):
            start += cols - 1
            if allWords[start % len(allWords)] == " ":
                start += 1
            elif allWords[(start + 1) % len(allWords)] == " ":
                start += 2
            else:
                while start > 0 and allWords[(start - 1) % len(allWords)] != " ":
                    start -= 1
        return start // len(allWords)
