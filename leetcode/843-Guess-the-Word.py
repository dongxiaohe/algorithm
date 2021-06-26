class Solution:
    def findSecretWord(self, wordlist, master):
        counter = [None] * 6
        for i in range(6): counter[i] = Counter(map(lambda x: x[i], wordlist)) 
        for _ in range(10):
            score, guess = 0, ""
            for word in wordlist:
                tmpScore = 0
                for i in range(6): tmpScore += counter[i][word[i]]
                if tmpScore > score:
                    score = tmpScore
                    guess = word
            # print(score, guess, wordlist)
            number = master.guess(guess)
            wordlist = [w for w in wordlist if sum([x == y for x, y in zip(guess, w)]) == number]
