class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def _dfs(node, low, high):
            if node:
                if node.val >= low and node.val <= high:
                    return node.val + _dfs(node.left, low, high) + _dfs(node.right, low, high)
                elif node.val < low:
                    return _dfs(node.right, low, high)
                else:
                    return _dfs(node.left, low, high)
            return 0
        return _dfs(root, low, high)

