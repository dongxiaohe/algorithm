def inOrder(node):
    result = []
    if node:
        result = inOrder(node.left)
        result.append(node.val)
        result.extend(inOrder(node.right))
    return result


