class Solution:
    res = 0
    def findTilt(self, root: TreeNode) -> int:
        def _findTilt(root: TreeNode) -> int:
            if root is None: return 0
            if root.left is None and root.right is None:
                return root.val
            left = _findTilt(root.left)
            right = _findTilt(root.right)
            self.res += abs(left - right)
            return left + right + root.val
        _findTilt(root)
        return self.res
