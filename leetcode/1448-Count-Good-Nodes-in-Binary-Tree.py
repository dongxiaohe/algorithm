class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def _goodNodes(node, _max):
            if node:
                if node.val >= _max:
                    return 1 + _goodNodes(node.left, node.val) + _goodNodes(node.right, node.val)
                return _goodNodes(node.left, _max) + _goodNodes(node.right, _max)
            return 0
        if root is None: return 0
        return _goodNodes(root, float("-inf"))
