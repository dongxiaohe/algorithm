class Solution:
    def deleteNode(self, node):
        while node.next: # precondition
            node.val = node.next.val
            pre = node
            node = node.next
        pre.next = None
