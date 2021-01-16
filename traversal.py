def inOrder(node):
    result = []
    if node:
        result = inOrder(node.left)
        result.append(node.val)
        result.extend(inOrder(node.right))
    return result

def preOrder(node):
    result = []
    if node:
        result.append(node.val)
        result.extend(preOrder(node.left))
        result.extend(preOrder(node.right))
    return result

