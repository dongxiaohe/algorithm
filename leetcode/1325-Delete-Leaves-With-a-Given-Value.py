class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root: 
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            if root.val == target and root.left is None and root.right is None:
                return None
            elif root.left is None and root.right is None:
                return root
        return root
