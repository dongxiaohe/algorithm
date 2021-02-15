class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def _isValidBST(node, _min, _max):
            if not node: return True
            if node.val <= _min or node.val >= _max: return False
            return _isValidBST(node.left, _min, node.val) and _isValidBST(node.right, node.val, _max)
        return _isValidBST(root, float("-inf"), float("inf")
