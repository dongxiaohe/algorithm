class Solution:
    _min = float("inf")
    prev = None
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return self._min
        self.minDiffInBST(root.left)
        if self.prev is not None:
            self._min = min(self._min, abs(root.val - self.prev))
        self.prev = root.val
        self.minDiffInBST(root.right)
        return self._min

