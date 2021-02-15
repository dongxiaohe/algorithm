class Solution(object):
    def isValidBST(self, root):
        if not root: return True
        stack, pre = [], None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val >= root.val: return False
            pre, root = root, root.right
        return True

