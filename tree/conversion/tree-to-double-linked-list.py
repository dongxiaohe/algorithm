def joinNodes(front, back):
    front.right = back
    back.left = front

def mergeNodes(front, back):
    if front is None: return back
    if back is None: return front
    frontLast = front.left
    backLast = back.left
    print("mergeNodes: ", front.val, back.val, frontLast.val, backLast.val)
    joinNodes(frontLast, back)
    joinNodes(backLast, front)
    return front

def treeToList(root):
    if root is None: return root
    ll = treeToList(root.left)
    lr = treeToList(root.right)
    if ll and lr:
        print(ll.val, lr.val, root.val)
    elif ll:
        print(ll.val, root.val)
    elif lr:
        print(lr.val, root.val)
    else:
        print("None", root.val)
    
    root.left = root.right = root
    return mergeNodes(mergeNodes(ll, root), lr)

from fixture import *
root = treeToList(three)
i, limit = 0, 5 
while i < limit:
    print("..................... " + root.val)
    root = root.right
    i += 1



