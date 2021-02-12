class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        swap1, swap2 = None, None
        tmp = head
        count = 1 
        while tmp:
            if count == k:
                swap1 = tmp
            if count == n - k + 1:
                swap2 = tmp
            tmp = tmp.next
            count += 1
        swap1.val, swap2.val = swap2.val, swap1.val
        return head
