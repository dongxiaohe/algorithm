class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, rev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
        return True

