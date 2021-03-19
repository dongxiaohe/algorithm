class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        _type = 0
        if ruleKey == "type":
            _type = 0
        elif ruleKey == "color":
            _type = 1
        else:
            _type = 2
        res = 0
        for item in items:
            if item[_type] == ruleValue:
                res += 1
        return res

