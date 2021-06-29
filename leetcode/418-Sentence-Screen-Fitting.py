class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        cnt, curLine, curCnt, lines = 0, "", 0, 1
        i = 0
        while True:
            index = i % len(sentence)
            if len(sentence[index]) + curCnt > cols:
                lines += 1
                curCnt = 0
            if lines > rows:
                i -= 1
                break
            if len(sentence[index]) + curCnt <= cols:
                curCnt += len(sentence[index]) + 1
            else: continue
            if curCnt > 0 and lines < rows and index == len(sentence) - 1 and curCnt + len(sentence[0]) > cols:
                i = (rows // lines) * (i + 1)
                lines *= (rows // lines)
                lines += 1
                curCnt = 0
                i -= 1
            i += 1
        return (i + 1) // len(sentence)
