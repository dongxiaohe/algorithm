class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(node, endNode):
            prev = None
            while node != endNode or node != None:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        slow = reverse(slow, None)
        fast = head
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
        
