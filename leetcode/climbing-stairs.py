class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        f_prev = 1 # 0
        f = 1 # 1
        
        for i in range(2, n + 1):
            new = f_prev + f
            f_prev, f = f, new
            
        return new
        