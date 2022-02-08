from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Input/Problem:
            int[][] - bits, square, mutable
            valid = all cells > main diagonal == 0
            
        Output:
            min(swaps) to get valid, or -1
            
        Intuition:
            each col - need to see >= +1 zeros than prev (starts at 0) in the rows
                aka = num_zeros_needed = col_index
                
            DP
            
        EC:
            rectangular matrix
            non-binary
            TODO
            
        Approach:
            1) DIY:
                A: fail fast - check all rows to see if >= num_zeros_needed
                B: brute force
                    - try all permutations of row_indices
                    - when one works
                    
            2) Sorting:
                A: mark the position of the last 1 in each row
                B: bubble sort the array
                C: give output:
                    if elems == indicies ==> return num_swaps
                    else ==> return -1
        """
        ### HELPERS
        def _locate_ones(grid):
            last_one_in_rows = list()
            for row in grid:
                for col_index in range(len(row) - 1, -1, -1):
                    if row[col_index] == 1:
                        last_one_in_rows.append(col_index)
                        break
            return last_one_in_rows

        def _bubble_sort(nums: List[int]) -> int:
            """return num_swaps"""
            is_sorted, num_swaps_overall = False, 0
            # sort the array
            while is_sorted is False:
                index, num_swaps = 0, 0
                while index < len(nums) - 1:
                    index2 = index + 1
                    if nums[index] > nums[index2]:
                        # swap - in the array AND the grid
                        nums[index], nums[index2] = nums[index2], nums[index]
                        grid[index], grid[index2] = grid[index2], grid[index]
                        num_swaps += 1
                    index += 1
                # should we continue?
                if num_swaps == 0:
                    is_sorted = True
                # update global count
                num_swaps_overall += num_swaps
            return num_swaps_overall

        ### MAIN
        # A: mark the position of the last 1 in each row
        last_one_in_rows = _locate_ones(grid)
        # B: bubble sort the array
        num_swaps = _bubble_sort(last_one_in_rows)
        # C: check the number of zeroes in each row
        for row_index in range(len(grid)):
            exp_zeros = len(grid) - 1 - row_index
            actual_num_zeros = len([val for val in grid[row_index] if val == 0])
            if actual_num_zeros < exp_zeros:
                return -1
        # grid is now valid!
        return num_swaps
