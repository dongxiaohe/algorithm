class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return 0, None
            left_level, left_node = dfs(node.left)
            right_level, right_node = dfs(node.right)
            if left_level == right_level: 
                return left_level + 1, node
            elif left_level > right_level:
                return left_level + 1, left_node
            else:
                return right_level + 1, right_node
        return dfs(root)[1]
