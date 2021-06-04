class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        kv, firstCity = {}, None
        for x, y in paths:
            if not firstCity: firstCity = x
            kv[x] = y
        while firstCity in kv:
            firstCity = kv[firstCity]
        return firstCity
