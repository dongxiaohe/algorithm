#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#
#For example, given the following Node class

from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def _serialize(root, result):
        if not root:
            result.append(None)
            return
        result.append(root.val)
        _serialize(root.left, result)
        _serialize(root.right, result)
    result = deque()
    _serialize(root, result)
    return result

def deserialize(data):
    if not data:
        return
    val = data.popleft()
    if val == None:
        return None
    node = Node(val)
    node.left = deserialize(data)
    node.right = deserialize(data)
    return node
        
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
