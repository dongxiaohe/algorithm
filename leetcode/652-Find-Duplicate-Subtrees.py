class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def tuplify(root):
            if root:
                key = root.val, tuplify(root.left), tuplify(root.right)
                kv[key].append(root)
                return key
        kv = defaultdict(list)
        tuplify(root)
        return [val[0] for val in kv.values() if len(val) > 1]
