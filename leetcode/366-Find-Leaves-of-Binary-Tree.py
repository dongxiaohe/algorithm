class Solution(object):
    def findLeaves(self, root):
        def _isLeaf(node):
            return node is not None and node.left is None and node.right is None
        def _dfs(node, res):
            if node is None: return None
            if _isLeaf(node.left):
                res.append(node.left.val)
                node.left = None
            if _isLeaf(node.right):
                res.append(node.right.val)
                node.right = None
            _dfs(node.left, res)
            _dfs(node.right, res)
        res, arr = [], []
        while not _isLeaf(root):
            _dfs(root, arr)
            res.append(arr)
            arr = []
        if root is not None: res.append([root.val])
        return res
