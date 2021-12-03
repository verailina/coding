"""
10 1 1 5 1 6
"""

class Solution:
    def rob_1(self, nums: List[int]) -> int:

        
        prev_true = nums[0]
        prev_false = 0
        
        for num in nums[1:]:
            new_true = prev_false + num
            new_false = max(prev_true, prev_false)
            
            prev_true, prev_false = new_true, new_false
        
        return max(prev_true, prev_false)
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(self.rob_1(nums[1:]), self.rob_1(nums[:-1]))
    
        
        
        
        