class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = ListNode(0)
        head.next = list1
        for i in range(a - 1):
            list1 = list1.next
        second = list1
        for i in range(b - a + 1):
            list1 = list1.next
        second.next = list2
        while second.next:
            second = second.next
        second.next = list1.next
        return head.next

