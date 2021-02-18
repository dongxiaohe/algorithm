class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return -1
        arr, res = [root], 0
        while arr:
            tmp, res = [], 0
            for node in arr:
                res += node.val
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            arr = tmp
        return res

