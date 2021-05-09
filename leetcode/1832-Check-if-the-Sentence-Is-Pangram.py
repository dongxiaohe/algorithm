class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = collections.Counter(string.ascii_lowercase)
        for ch in sentence:
            counter[ch] += 1
        for key in counter.keys():
            if counter[key] <= 1:
                return False
        return True
