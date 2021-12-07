# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _rob(self, root: Optional[TreeNode]) -> Tuple[int]:
        if root is None:
            return 0, 0
        rob_left_true, rob_left_false = self._rob(root.left)
        rob_right_true, rob_right_false = self._rob(root.right)
        
        rob_true = root.val + rob_left_false + rob_right_false
        rob_false = max([rob_left_false + rob_right_false,
                         rob_left_true + rob_right_false,
                         rob_left_false + rob_right_true,
                         rob_left_true + rob_right_true])
        
        return rob_true, rob_false
        
        
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self._rob(root))
        