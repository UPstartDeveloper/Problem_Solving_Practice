from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        """
        Input/Problem:
            Leetcode: https://leetcode.com/problems/projection-area-of-3d-shapes/
            
            2d int[]
            non-empty
            pos num
            each block has the coords:
                x, y, z = i, j, v = grid[i, j]
            
            "top" = xy
            "front" = yz
            "side" = xz
            
            # towers = n x n
            
            [
                [1,2],
                [3,4]
            ]
            
            Getting the Area:
                1) xy plane = 1 X (n x n)
                2) yz plane = n x max_of_each col
                3) xz plane = n x max_of_each row
            
        """
        ### HELPERS
        def _scalar_multiply(coef, arr):
            return sum([elem for elem in arr])

        def _max_col_wise(grid):
            highest_vals = list()
            for col_index in range(len(grid[0])):
                highest = float("-inf")
                for row_index in range(len(grid)):
                    highest = max(highest, grid[row_index][col_index])
                highest_vals.append(highest)
            return highest_vals

        def _max_row_wise(grid):
            return [max(row) for row in grid]

        def _count_towers():
            towers = 0
            for row in grid:
                for tower_height in row:
                    if tower_height > 0:
                        towers += 1
            return towers

        ### MAIN
        n = len(grid)
        xy_area = _count_towers()
        max_of_cols = _max_col_wise(grid)
        yz_area = _scalar_multiply(n, max_of_cols)
        max_of_rows = _max_row_wise(grid)
        xz_area = _scalar_multiply(n, max_of_rows)

        return xy_area + yz_area + xz_area
