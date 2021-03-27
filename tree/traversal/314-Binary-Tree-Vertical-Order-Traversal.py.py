class Solution(object):
    def verticalOrder(self, root):
        if not root: return []
        kv = collections.defaultdict(list)
        level = [(root, 0)]
        while level:
            tmp = []
            for node, i in level:
                kv[i].append(node)
                if node.left: tmp.append([node.left, i - 1])
                if node.right: tmp.append([node.right, i - 1])
            level = tmp
        offset, res = -min(kv.keys), [0] * len(kv)
        for k, v in kv.items():
            res[k + offset] = v
        return res
