class Solution:
    count = 0
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def _dfs(node, distance):
            if not node: return []
            if not node.left and not node.right: return [1]
            left = _dfs(node.left, distance)
            right = _dfs(node.right, distance)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.count += 1 
            tmp = []
            for n in left + right:
                if n + 1 < distance:
                    tmp.append(n + 1)
            return tmp
        _dfs(root, distance)
        return self.count
