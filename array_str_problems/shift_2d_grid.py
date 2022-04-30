from collections import deque


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Problem: https://leetcode.com/problems/shift-2d-grid/
        Input:
            int[][] - mutable, rect (mxn), non empty, pos/neg
            k - shifts, non neg
            
        Output:
            modified matrix
            
        Intuition:
            psuhed over all but last col
            last col - would use a deque? (assume yes)
                becomes first col
                last col elem goes to the top
                rest move down
        
        EC: 
            - invalid inputs -> ValueError?
                - jagged matrix
                - empty matrix
                - invalid k,n,m
            - all dupe elems - early out
            - TODO
            
        Approaches:
        
            1) Brute force --> O(k * m * n), O(n)
                run the simulation
            
            2) more intuitive:
                if k/n == m ---> return matrix right away O(1)
                else, use k/n --> # of row rotations to do - O(mxn)
                if k % n > 0:
                    then we do (k % n) shift ops  - O(m * n * n)
        
        """
        ### HELPERS
        def _rotate_rows(grid):
            """TODO"""
            last_row = grid[-1][:]
            for row_index in range(len(grid) - 1, 0, -1):
                for col_index in range(len(grid[0])):
                    grid[row_index][col_index] = grid[row_index - 1][col_index]
            grid[0] = last_row

        def _shift_once(grid):
            last_col = deque([grid[row][-1] for row in range(len(grid))])
            last_col.appendleft(last_col.pop())
            # shift other cols by 1 -->
            for col_index in range(len(grid[0]) - 1, 0, -1):
                for row_index in range(len(grid)):
                    grid[row_index][col_index] = grid[row_index][col_index - 1]
            # overwrite the first col
            for row_index in range(len(grid)):
                grid[row_index][0] = last_col[row_index]

        ### DRIVER
        # TODO: validate inputs
        # A: if k/n == m ---> return matrix right away O(1)
        n, m = len(grid[0]), len(grid)
        if (k / n) == m:
            return grid
        # B: else, use k/n --> # of row rotations to do - O(k * m * n)
        for _ in range(k // n):
            _rotate_rows(grid)
        # C: if k % n > 0:
        if k % n > 0:
            for _ in range((k % n)):  # - O(m * n * n)
                _shift_once(grid)
        return grid
