class Solution(object):
    def findLeaves(self, root):
        def _isLeaf(node):
            if node is None: return False
            return node.left is None and node.right is None
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
        if _isLeaf(root):
            arr.append(root.val)
            res.append(arr)
            return res
        while root is not None:
            _dfs(root, arr)
            res.append(arr)
            arr = []
            if _isLeaf(root):
                arr.append(root.val)
                res.append(arr)
                return res
        return res
