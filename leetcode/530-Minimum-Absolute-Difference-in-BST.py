class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = {
            "prev": None,
            "cur": None,
            "_min": float("inf")
        }
        def _inorder(node, res):
            if node:
                _inorder(node.left, res)
                if res["prev"] is None:
                    res["prev"] = node.val
                elif res["cur"] is None:
                    res["cur"] = node.val
                    res["_min"] = min(res["_min"], abs(res["cur"] - res["prev"]))
                else: 
                    res["prev"] = res["cur"]
                    res["cur"] = node.val
                    res["_min"] = min(res["_min"], abs(res["cur"] - res["prev"]))
                _inorder(node.right, res)
        _inorder(root, res)
        return res["_min"]
    
