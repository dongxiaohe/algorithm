class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        power, res = 0, 0
        while stack:
            res += 2 ** power if stack.pop() else 0
            power += 1
        return res
