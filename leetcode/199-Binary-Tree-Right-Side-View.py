class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(node, depth, res):
            if not node: return
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, depth + 1, res)
            dfs(node.left, depth + 1, res)
        res = []
        dfs(root, 0, res)
        return res
