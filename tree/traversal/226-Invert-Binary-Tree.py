class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            tmp1 = self.invertTree(root.right)
            tmp2 = self.invertTree(root.left)
            root.left = tmp1
            root.right = tmp2
            return root

