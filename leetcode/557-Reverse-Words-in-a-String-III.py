class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        return " ".join(map(lambda x:x[::-1], words))
