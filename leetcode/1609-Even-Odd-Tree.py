class Solution(object):
    def isEvenOddTree(self, root):
        def _preTraversal(root, kv, level):
            if not root:
                return
            kv[level].append(root.val)
            _preTraversal(root.left, kv, level + 1)
            _preTraversal(root.right, kv, level + 1)
        kv = collections.defaultdict(list)
        _preTraversal(root, kv, 0)
        for level, arr in kv.items():
            if level % 2 == 0 and arr != sorted(arr):
                return False
            elif level % 2 == 1 and arr != sorted(arr):
                return False
        return True

