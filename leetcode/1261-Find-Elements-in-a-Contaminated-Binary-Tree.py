class FindElements:
    def __init__(self, root: TreeNode):
        self.root = root
        def dfs(node, value):
            if not node: return
            node.val = value
            dfs(node.left, node.val * 2 + 1)
            dfs(node.right, node.val * 2 + 2)
        dfs(root, 0) 
    def find(self, target: int) -> bool:
        node = self.root
        binary = list(bin(target + 1)[3:])
        while node: 
            if node.val == target:
                return True
            bit = binary.pop(0)
            if bit == "0":
                node = node.left
            else:
                node = node.right
        return False
