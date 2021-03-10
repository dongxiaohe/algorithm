class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def _sum(node, val):
            if not node: return 0
            val = 2 * val + node.val
            if node.left == node.right == None: return val
            return _sum(node.left, val) + _sum(node.right, val)

        return _sum(root, 0)
