class Node:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.total = 0
        self.start = start
        self.end = end

class NumArray(object):

    def __init__(self, nums):
        def buildTree(nums, left, right):
            root = Node(left, right)
            if left == right:
                root.total = nums[left]
                return root
            mid = left + (right - left >> 1)
            root.left = buildTree(nums, left, mid)
            root.right = buildTree(nums, mid + 1, right)
            root.total = root.left.total + root.right.total
            return root
        self.root = buildTree(nums, 0, len(nums) - 1)

    def update(self, index, val):
        def updateTree(root, i, val):
            start, end = root.start, root.end 
            if start == end == i:
                root.total = val
                return root
            mid = start + (end - start >> 1)
            if i <= mid:
                updateTree(root.left, i, val)
            else:
                updateTree(root.right, i, val)
            root.total = root.left.total + root.right.total
            return root.total
        updateTree(self.root, index, val)

    def sumRange(self, left, right):
        def sumTree(root, left, right):
            start, end = root.start, root.end
            if start == left and end == right:
                return root.total
            mid = start + (end - start >> 1)
            if right <= mid:
                return sumTree(root.left, left, right)
            elif left > mid:
                return sumTree(root.right, left, right)
            else:
                return sumTree(root.left, left, mid) + sumTree(root.right, mid + 1, right)
        return sumTree(self.root, left, right)
