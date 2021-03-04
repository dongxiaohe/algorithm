class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def _pushLeft(stack, node):
            while node:
                stack.append(node)
                node = node.left
        s1, s2, res = [], [], []
        _pushLeft(s1, root1)
        _pushLeft(s2, root2)
        while s1 or s2:
            s = None
            if s1 and s2:
                s = s1 if s1[-1].val < s2[-1].val else s2
            else:
                s = s1 if s1 else s2
            node = s.pop()
            res.append(node.val)
            _pushLeft(s, node.right)
        return res
