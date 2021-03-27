class Solution(object):
    self.res = None
    def inorderSuccessor(self, root, p):
        def _binarySearch(node, p, _next):
            if not node: return
            if p.val < node.val <= _next:
                self.res = node
                _binarySearch(node.left, p, node.val)
            elif p.val > node.val:
                _binarySearch(node.right, p, _next)
            else:
                _binarySearch(node.left, p, _next)
        _binarySearch(root, p, float("inf"))
        return self.res

