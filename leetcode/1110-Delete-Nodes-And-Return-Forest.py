class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        toDeletes, res = set(to_delete), []
        def _delNodes(node, isRootDeleted):
            if not node: return None
            deleted = node.val in toDeletes
            if isRootDeleted and not deleted:
                res.append(node)
            node.left = _delNodes(node.left, deleted)
            node.right = _delNodes(node.right, deleted)
            return None if deleted else node
        _delNodes(root, True)
        return res
