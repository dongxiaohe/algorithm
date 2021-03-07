class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level, nodes, _max, res = 1, [root], float("-inf"), -1
        while nodes:
            tmp, _sum = [], 0
            for node in nodes:
                _sum += node.val
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            if _sum > _max:
                res = level
                _max = _sum
            nodes = tmp
            level += 1
        return res
