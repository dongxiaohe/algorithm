class Solution(object):
    def isEvenOddTree(self, root):
        queue = collections.deque()
        queue.append(root)
        even = True
        while queue:
            size = len(queue)
            if even: preVal = float("-inf")
            else: preVal = float("inf")
            while size > 0: # use queue and size to travere by the levels
                node = queue.popleft()
                if even and (node.val % 2 == 0 or preVal >= node.val):return False
                if not even and (node.val % 2 == 1 or preVal <= node.val): return False
                preVal = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                size -= 1
            even = not even
        return True
