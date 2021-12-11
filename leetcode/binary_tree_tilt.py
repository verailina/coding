from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tilt_sum = 0
        
    def findSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_sum = self.findSum(root.left)
        right_sum = self.findSum(root.right)
        self.tilt_sum += abs(left_sum - right_sum)
        return root.val + left_sum + right_sum
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.findSum(root)
        return self.tilt_sum
        