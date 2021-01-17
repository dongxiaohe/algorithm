from fixture import *

def inOrder(node):
    result = []
    if node:
        result.extend(inOrder(node.left))
        result.append(node.val)
        result.extend(inOrder(node.right))
    return result

def inOrderIter(node):
    stack, result = [], []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        cur = stack.pop()
        result.append(cur.val)
        node = cur.right
    return result

def preOrder(node):
    result = []
    if node:
        result.append(node.val)
        result.extend(preOrder(node.left))
        result.extend(preOrder(node.right))
    return result

def preOrderIter(node):
    if not node: return []
    stack, result = [node], []
    while stack:
        cur = stack.pop()
        result.append(cur.val)
        if cur.right: stack.append(cur.right)
        if cur.left: stack.append(cur.left)
    return result

def postOrder(node):
    result = []
    if node:
        result.extend(postOrder(node.left))
        result.extend(postOrder(node.right))
        result.append(node.val)
    return result

assert inOrder(root) == inOrderIter(root)
assert preOrder(root) == preOrderIter(root)
