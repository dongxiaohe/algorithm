class Codec:
    def encode(self, strs: [str]) -> str:
        res = []
        for each in strs:
            res.append(str(len(each)) + "/" + each)
        return "".join(res)
    def decode(self, s: str) -> [str]:
        i, m = 0, len(s)
        res = []
        while i < m: 
            slash = s.index("/", i)
            size = int(s[i:slash])
            res.append(s[slash + 1: slash + 1 + size])
            i = slash + size + 1 
        return res
