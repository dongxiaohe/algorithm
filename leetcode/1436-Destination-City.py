class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        kv, initial = {}, None
        for x, y in paths:
            if not initial: initial = x
            kv[x] = y
        while initial in kv:
            initial = kv[initial]
        return initial
