class Solution(object):
    def uniqueMorseRepresentations(self, words):
        keys = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            morse = ""
            for ch in word:
                morse += keys[ord(ch) - 97]
            res.add(morse)
        return len(res)
