class Solution:
    xParent = None
    yParent = None
    xLevel = -1
    yLevel = -1
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, x, y, level, root):
            if not node: return 
            if node.val == x:
                self.xParent = root
                self.xLevel = level
            if node.val == y:
                self.yParent = root
                self.yLevel = level
            dfs(node.left, x, y, level + 1, node)
            dfs(node.right, x, y, level + 1, node)
        dfs(root, x, y, 0, None)
        return self.xLevel == self.yLevel and self.xParent != self.yParent

