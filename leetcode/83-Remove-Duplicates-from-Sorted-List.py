class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = head
        while head:
            cur = head
            while head.next and cur.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return res
