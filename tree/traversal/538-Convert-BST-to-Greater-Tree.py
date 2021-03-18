class Solution:
    val = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        if root.right: self.convertBST(root.right)
        root.val = self.val = self.val + root.val
        if root.left: self.convertBST(root.left)
        return root
