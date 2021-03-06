def treeToList(root):
    stack, pre, cur, first = [], None, root, None
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        cur = stack.pop()
        if pre is not None:
            if first is None: first = cur
            pre.right = cur
            cur.left = pre
        pre = cur
        root = cur.right
    first.left = cur
    cur.right = first
    return first

from fixture import *
root = treeToList(three)

i, limit = 0, 6 
while i < limit:
    print("..................... " + root.val)
    root = root.right
    i += 1

