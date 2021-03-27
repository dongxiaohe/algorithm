class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur, head, prev = root, None, None
        while cur:
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            cur, head, prev = head, None, None 
        return root

