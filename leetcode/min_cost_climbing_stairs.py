class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = 0 # 1
        prev1 = min(cost[0], cost[1]) # 2
        
        for i in range(3, len(cost) + 1):
            sol = min(cost[i - 1] + prev1, cost[i - 2] + prev2)
            prev1, prev2 = sol, prev1
            
        return prev1