class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        while p:
            if not p.child:
                p = p.next
                continue
            tmp = p.child
            while tmp.next:
                tmp = tmp.next
            tmp.next = p.next
            if p.next: p.next.prev = tmp
            p.next = p.child
            p.child.prev = p
            p.child = None
        return head
