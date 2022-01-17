from cmath import exp
from typing import List


class Solution:
    def min_cost_to_paint(self, paint_costs: List[List[int]]) -> int:
        """
        Suppose there's a shed full of bikes, 
        and you need to paint them all before selling them. 
        
        The bikes can all be painted one of 3 colors:
            1. green
            2. blue
            3. red
        
        Each color has a certain cost associated with it. 
        Additionally, no two adjacent bikes can be painted the same color 
            (e.g. you can't use the same color 2x in a row).

        We can represent the cost of painting each bike through 
        - a matrix that will be of n x 3 shape. 
        
        For example, cost[0][0] represents the cost of painting the first bike green, 
                     cost[2][2] represents the cost of painting the third bike red.

        
        Given this information, write a function that 
        ****returns the minimum cost of painting the bikes.****
        
        Example Input: 
        
        [
            [3,2,4],
            [3,4,6]
        ]

        Poss combos:
            0, 1
            0, 2
            1, 0
            1, 2
            2, 0,
            2, 1
    
        Example Output: 5
        
        Explanation:
            Here we would paint the first bike with the second color, blue, 
            since $2 is the minimum cost, and 
            
            we would paint the second house with the first color, green, 
            since that represents the minimum cost and will not be painted 
            the same color as the bike to the left of it.


        Input/Problem:
            - n x 3 int matrix pos immutable
            - need to "choose" a color index, 
                based on min total_cost
                AND cannot reuse the same index 2x in a row
            - Insight: <choosinge NDX based on PRICE>

        Output:
            min_total_cost

        Intuition:
            1. heaps
            2. dynamic programming
            3. permutations/backtracking

        EC:
            1. all prices >= 0? doesn't matter
            2. invalid price (e.g. str) --> ValueError
            3. invalid matrix? --> ValueError
                - no rows
                - jagged, not all rows have exactly 3 columns
            4. too big matrix?
                - assume it fits in memory

        Approach: 
            1. SEE BELOW
                Time: O(n * 3^n)
                Space: O(n)

        """
        ### HELPERS
        def _solve_using_backtracking(current_row, colors_chosen):
            # Base Case: outside the matrix
            if current_row == len(paint_costs):
                # compute total
                total_current_cost = 0
                for bike_index, color_chosen in enumerate(colors_chosen):
                    total_current_cost += paint_costs[bike_index][color_chosen]
                # update min
                if total_current_cost < self.min_cost:
                    self.min_cost = total_current_cost
            # Recursive case: choose next color
            else:  # current_row < len(paint_costs)
                # color_costs = paint_costs[current_row]
                for index in range(3):
                    # cost = color_costs[index]
                    if (current_row == 0) or (
                        len(colors_chosen) > 0 and index != colors_chosen[-1]
                    ):
                        # pick the color, and recurse
                        colors_chosen.append(index)
                        _solve_using_backtracking(current_row + 1, colors_chosen)
                        # TODO[test]: pop the last added
                        colors_chosen.pop()
            # All done!
            return self.min_cost

        ### MAIN
        # TODO: Check Edge Cases
        pass
        # Solution 1
        self.min_cost = float("inf")
        return _solve_using_backtracking(0, list())


if __name__ == "__main__":
    solver = Solution()
    tests = [
        # input           exp output
        ([[3, 2, 4], [3, 4, 6]], 5)
    ]
    for matrix, exp_output in tests:
        actual = solver.min_cost_to_paint(matrix)
        assert exp_output == actual, f"Actual: {actual}, Expected: {exp_output}"
