class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justifyLine(arr, maxWidth, lastLine):
            if len(arr) == 1: return arr[0] + " " * (maxWidth - len(arr[0]))
            if lastLine: 
                firstSection = " ".join(arr)
                return firstSection + " " * (maxWidth - len(firstSection))
            spaces = len(arr) - 1
            leftSpaces = maxWidth - len("".join(arr))
            if leftSpaces % spaces == 0:
                return (" " * (leftSpaces // spaces)).join(arr)
            additionSpacesCnt = (leftSpaces % spaces)
            for i in range(len(arr)):
                if additionSpacesCnt == 0:
                    return (" " * (leftSpaces // spaces)).join(arr)
                else:
                    arr[i] += " "
                    additionSpacesCnt -= 1     
        res, curLine, curCount = [], [], 0
        for i in range(len(words)):
            if curCount == 0 or len(words[i]) + curCount <= maxWidth:
                curLine.append(words[i])
                curCount += len(words[i]) + 1
            else:
                res.append(justifyLine(curLine, maxWidth, False))
                curLine = [words[i]]
                curCount = len(words[i]) + 1
        if curLine:
            res.append(justifyLine(curLine, maxWidth, True))
        return res
