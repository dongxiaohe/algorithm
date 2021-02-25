class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def _inorder(node):
            result = []
            if node:
                result.extend(_inorder(node.left))
                if node.left == node.right == None:
                    result.append(node.val)
                result.extend(_inorder(node.right))
            return result
       return _inorder(root1) == _inorder(root2) 
