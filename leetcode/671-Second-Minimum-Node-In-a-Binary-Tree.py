class Solution:
    _min1, _min2 = None, None
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root:
            if self._min1 is None:
                self._min1 = root.val
            elif root.val > self._min1:
                self._min2 = min(root.val, self._min2 if self._min2 else float("inf"))
            elif root.val < self._min1:
                self._min2 = self._min1
                self._min1 = root.val
            self.findSecondMinimumValue(root.left)
            self.findSecondMinimumValue(root.right)
        return self._min2 if self._min2 else -1

