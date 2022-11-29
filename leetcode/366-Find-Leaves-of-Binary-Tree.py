class Solution(object):
    def findLeaves(self, root):
        def _dfs(node, res):
            if node is None: return -1
            level = 1 + max(_dfs(node.left, res), _dfs(node.right, res))
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            return level
        res = []
        _dfs(root, res)
        return res

