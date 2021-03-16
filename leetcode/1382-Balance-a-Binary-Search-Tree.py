class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def _inorderTraversal(node):
            result = []
            if not node: return result
            result.extend(_inorderTraversal(node.left))
            result.append(node.val)
            result.extend(_inorderTraversal(node.right))
            return result
        def _bst(nodes):
            if not nodes:
                return None
            mid = len(nodes) >> 1
            root = TreeNode(nodes[mid])
            root.left = _bst(nodes[:mid])
            root.right = _bst(nodes[mid + 1:])
            return root
        nodes = _inorderTraversal(root)
        return _bst(nodes)
