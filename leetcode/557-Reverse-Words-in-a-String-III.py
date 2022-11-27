class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        return " ".join(word[::-1] for word in words.split(" "))

