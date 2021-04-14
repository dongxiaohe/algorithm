class Solution:
    cnt = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandParent):
            if not node: return
            if grandParent and grandParent.val & 1 == 0:
                self.cnt += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        dfs(root, None, None)
        return self.cnt
