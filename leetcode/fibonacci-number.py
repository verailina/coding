class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        f_n_1 = 1
        f_n_2 = 0
        
        for i in range(2, n + 1):
            new = f_n_1 + f_n_2
            f_n_2 = f_n_1
            f_n_1 = new
            
        return f_n_1