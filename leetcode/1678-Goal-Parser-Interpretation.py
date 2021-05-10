class Solution:
    def interpret(self, command: str) -> str:
        tmp, res = "", []
        kv = {"G":"G", "()":"o", "(al)":"al"}
        for ch in command:
            tmp += ch
            if tmp in kv:
                res.append(kv[tmp])
                tmp = ""
        return "".join(res)
