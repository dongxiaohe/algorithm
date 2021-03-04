class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def _inorder(node):
            result = []
            if node:
                result.extend(_inorder(node.left))
                result.append(node.val)
                result.extend(_inorder(node.right))
            return result
        res1, res2, res = _inorder(root1), _inorder(root2), []
        i = j = 0
        while i < len(res1) or j < len(res2):
            if i < len(res1) and j < len(res2):
                if res1[i] < res2[j]:
                    res.append(res1[i])
                    i += 1
                else:
                    res.append(res2[j])
                    j += 1
            elif i < len(res1):
                res.append(res1[i])
                i += 1
            else:
                res.append(res2[j])
                j += 1
        return res
                
