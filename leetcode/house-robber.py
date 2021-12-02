class Solution:
    def rob(self, nums: List[int]) -> int:

        
        prev_true = nums[0]
        prev_false = 0
        
        for num in nums[1:]:
            new_true = prev_false + num
            new_false = max(prev_true, prev_false)
            
            prev_true, prev_false = new_true, new_false
        
        return max(prev_true, prev_false)
        
        