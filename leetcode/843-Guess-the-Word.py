class Solution:
    def findSecretWord(self, wordlist, master):
        for i in range(10):
            pivot = random.choice(wordlist)
            number = master.guess(pivot)
            wordlist = [w for w in wordlist if sum(x == y for x, y in zip(w, pivot)) == number]
