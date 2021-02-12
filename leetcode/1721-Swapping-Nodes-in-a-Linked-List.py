class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1, n2, p = None, None, head
        while p:
            k -= 1
            if n2: n2 = n2.next
            if k == 0:
                n1 = p
                n2 = head
            p = p.next
        n1.val, n2.val = n2.val, n1.val
        return head

