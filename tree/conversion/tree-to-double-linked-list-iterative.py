def treeToList(root):
    if root is None: return root
    prev, cur, first = None, None, None
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        cur = stack.pop() 
        if prev is not None:
            if not first: first = prev
            print(prev.val, cur.val)
            cur.left = prev
            prev.right = cur
        prev = cur
        root = cur.right
    first.left = cur
    cur.right = first
    return first


from fixture import *
root = treeToList(three)
i, limit = 0, 5 
while i < limit:
    print("..................... " + root.val)
    root = root.right
    i += 1



