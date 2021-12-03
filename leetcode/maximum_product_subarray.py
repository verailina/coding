class Solution:
    def compute_product(self, nums):
        product = 1
        for n in nums:
            product *= n
            
        return product
    
    def max_none(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        return max(a, b)
    
    def subsolve(self, nums):
        total = self.compute_product(nums)
        if total > 0:
            return total
        leftBest = total
        i = 0
        while leftBest < 0 and i < len(nums) - 1:
            leftBest /= nums[i]
            i += 1
        rightBest = total
        j = len(nums) - 1
        while rightBest < 0 and j > 0:
            rightBest /= nums[j]
            j -= 1
        
        return max(leftBest, rightBest)
    
    
    def maxProduct(self, nums: List[int]) -> int:
        best = None
        start, end = 0, None
        for i, num in enumerate(nums):
            if num == 0:
                end = i
                if start != end:
                    best = self.max_none(best, self.subsolve(nums[start:end]))
                start, end = i + 1, None
                best = self.max_none(best, 0)
                
        if start < len(nums):
            best = self.max_none(best, self.subsolve(nums[start:]))
            
        return int(best)
                    
        