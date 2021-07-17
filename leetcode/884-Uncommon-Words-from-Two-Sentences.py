class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter, cur, res = defaultdict(int), "", []
        for ch in s1 + " " + s2:
            if ch != " ": cur += ch
            elif ch == " ":
                counter[cur] += 1
                cur = ""
        if cur: counter[cur] += 1
        for word in counter:
            if counter[word] == 1:
                res.append(word)
        return res
