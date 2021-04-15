class Solution:
    cnt = 0
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.cnt += abs(left) + abs(right)
            return node.val + left + right - 1
        dfs(root)
        return self.cnt
