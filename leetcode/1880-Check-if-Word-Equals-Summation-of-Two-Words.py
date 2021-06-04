class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def calculate(word):
            base, acc = 1, 0
            for i in range(len(word) - 1, -1, -1):
                acc += (ord(word[i]) - 97) * base
                base *= 10
            return acc
        return calculate(firstWord) + calculate(secondWord) == calculate(targetWord)
