from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        """
        Credit to BotM: https://leetcode.com/problems/minimum-path-cost-in-a-grid/discuss/2188255/python3
        
        Time: O(rows * cols^2)
        Space: O(cols)
        """
        n = len(grid)
        m = len(grid[0])
        
        dp = grid[0][:]
        # traverse rows
        for next_row in range(1, n):
            # all the costs up to now, are indpndt of what's ahead
            prev = dp[:]
            dp = [float("inf")]*m  # init values
            # traverse cols
            for col2 in range(m):    
                # traverse only the min edge in the current col, to some col in next row
                for col1, val1 in enumerate(grid[next_row - 1]):
                    dp[col2] = min(
                        dp[col2], 
                        prev[col1] + moveCost[val1][col2] + grid[next_row][col2]
                    )
        return min(dp)
