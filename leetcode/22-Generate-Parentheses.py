class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _backtrack(maxOpen, opened, closed, arr, res):
            if len(arr) == 2 * maxOpen:
                res.append(arr)
                return
            if maxOpen > opened:
                _backtrack(maxOpen, opened + 1, closed, arr + "(", res)
            if opened > closed:
                _backtrack(maxOpen, opened, closed + 1, arr + ")", res)
        result = [] 
        _backtrack(n, 0, 0, "", result)
        return result
