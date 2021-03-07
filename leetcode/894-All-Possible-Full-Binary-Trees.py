class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        def _allPossibleFBT(n, mem):
            if n in mem: return mem[n]
            n -= 1
            if n == 0: return [TreeNode(0)]
            res = []
            for i in range(1, n, 2):
                for left in _allPossibleFBT(i, mem):
                    for right in _allPossibleFBT(n - i, mem):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.extend([root])
            mem[n] = res
            return res
        return _allPossibleFBT(n, {})
