class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        seen = collections.defaultdict(ListNode)
        prefix = 0
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        prefix = 0
        head = dummyHead
        while head:
            prefix += head.val
            if prefix in seen:
                head.next = seen[prefix].next
            head = head.next
        return dummyHead.next

