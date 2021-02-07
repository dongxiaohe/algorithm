class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = tmp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            tmp.next = ListNode(val)
            tmp = tmp.next
        return root.next
