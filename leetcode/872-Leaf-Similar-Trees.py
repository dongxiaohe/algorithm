class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        stack1, stack2 = [root1], [root2]
        def _dfs(stack):
            while True:
                node = stack.pop()
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                if node.left == node.right == None: return node.val
        while stack1 and stack2:
            if _dfs(stack1) != _dfs(stack2): return False
        return len(stack1) == len(stack2) == 0

