class Solution:
    def splitBST(self, root: TreeNode, target: int) -> List[TreeNode]:
        if not root: return [None, None]
        if root.val == target:
            a = root.right
            root.right = None
            return [root, a]
        elif root.val < target:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]
        else:
            left, right = self.splitBST(root.left, target)
            root.left = right
            return [left, root]
