class Solution:
    def maxAndIndex(self, arr):
        _max, position = float("-inf"), -1
        for i in range(len(arr)):
            if arr[i] > _max:
                _max = arr[i]
                position = i
        return (_max, position)
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        _max, position = self.maxAndIndex(nums)
        root = TreeNode(_max)
        root.left = self.constructMaximumBinaryTree(nums[:position])
        root.right = self.constructMaximumBinaryTree(nums[position + 1:])
        return root
