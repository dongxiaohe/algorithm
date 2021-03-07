class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        n -= 1
        if n == 0: return [TreeNode(0)]
        res = []
        for i in range(1, n, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n - i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.extend([root])
        return res
