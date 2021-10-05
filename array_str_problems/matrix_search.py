"""
Problem: return 1 if an element is found in a 2D array, and 0 if it's not

Clarifications:
- 2D with dims m x n
- each row (inner list) is sorted (least to greater)
- beginning of each row, starts off higher than the last
- Insight: this makes the rows of the array sorted, as well as the columns!

Assumptions:
- the matrix is not a square, so we have to actually search for the element before
   making a decision
   

Idea #1 - O(m * n)
- start iterating from first row
    - if found return 1
    - if last element is greater than target and not found, return 0
    - if we hit an element greater than target, before the end of row, move to next row
    
Idea #2 - O(m + n)
A: find the row
  - iterate down the first column
    - if a element is greater than target, then we know we might find it in the row above
    - search the row
  
Idea #3 - binary searches
- search the first column for the target, return the row we expect it to be in
- binary search the row

O(log m + log n) = O(log(m*n))
"""
import math


def matrix_search(matrix, target):
    # store a variable for the last column
    last_col = len(matrix[0]) - 1

    def find_row(lo_row, hi_row):
        """Finds the row in which the target most likely expected to be in"""
        # compare the value in the middle row to the value
        mid_row_index = int((lo_row + hi_row) / 2)
        print(mid_row_index)
        mid_row_first, mid_row_last = (
            matrix[mid_row_index][0],
            matrix[mid_row_index][last_col],
        )
        # if found, return the index of the row
        if mid_row_first <= target <= mid_row_last or lo_row == hi_row:
            return mid_row_index
        # if target less than middle row,
        elif target < mid_row_first:
            # search the lower half of the column
            return find_row(lo_row, mid_row_index - 1)
        # if target greater
        elif target > mid_row_last:
            # search the larger half of the column
            return find_row(mid_row_index + 1, hi_row)

    def search_row(low, hi, row):
        """Finds the element in the row (and returns 1), or returns 0."""
        # find the value in the middle
        mid_index = int((low + hi) // 2)
        middle = row[mid_index]
        # if equal, then return 1
        if target == middle:
            return 1
        # if not found, return 0
        elif low == hi:
            return 0
        # if less than, search the lower half of the row
        elif target < middle:
            return search_row(low, mid_index - 1, row)
        # if greater than, search the larger half of the row
        elif target > middle:
            return search_row(mid_index + 1, hi, row)

    # search the first column for the target
    row_expected_index = find_row(0, len(matrix) - 1)
    # get the row to search
    expected_row = matrix[row_expected_index]
    # search the row
    return search_row(0, last_col, expected_row)


if __name__ == "__main__":
    print(matrix_search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11))
