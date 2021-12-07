class Solution:
        
    def minCostToMoveChips(self, position: List[int]) -> int:
        costOdd, costEven = 0, 0
        for pos in position:
            if pos % 2 == 0:
                costOdd += 1
            else:
                costEven += 1
        return min(costOdd, costEven)