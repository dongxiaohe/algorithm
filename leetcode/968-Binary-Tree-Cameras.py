class Solution:
    count = 0
    def minCameraCover(self, root: TreeNode) -> int:
        def _dfs(node):
            if not node: return 2
            left = _dfs(node.left)
            right = _dfs(node.right)
            if left == 0 or right == 0:
                self.count += 1
                return 1
            if left == 1 or right == 1:
                return 2
            return 0

        return (_dfs(root) == 0) + self.count
