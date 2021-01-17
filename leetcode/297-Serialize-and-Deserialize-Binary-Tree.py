from collections import deque
class Codec:

    def serialize(self, root):
        def _preOrder(node):
            result = []
            if not node: result.append(None)
            else:
                result.append(node.val)
                result.extend(_preOrder(node.left))
                result.extend(_preOrder(node.right))
            return result
        return deque(_preOrder(root))

    def deserialize(self, data):
        if data:
            val = data.popleft()
            if val == None: return None
            root = TreeNode(val)
            root.left = self.deserialize(data)
            root.right = self.deserialize(data)
            return root

