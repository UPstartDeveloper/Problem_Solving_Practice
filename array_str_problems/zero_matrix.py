"""
Zero Matrix: 
Write an algorithm such that 

if an element in an MxN matrix is 0, 
its entire row and column are set to O.

Clarifying Questions and Assumptions: 
- so we have a rectangular matrix? yes
- just integers? yes
- and what are the inputs to the function?
    - are we given the indicies of a single element ---> use a helper function
    - or are we given the entire matrix, and expected to do this 
        over the whole matrix? yes
- is the input mutable? no ---> otherwise it'll be ambiguous about 
    - which rows and cols to "zeroify" as the function goes on
- are we guaranteed to have at least 1 row with at least 1 element? no
- are we allowed to use NumPy? no, you don't really need to 
- what is the return value --> a matrix?

Intuition:
- traverse the 2D matrix

Approach Ideas:

test input = 
[
    [0, 5 ,6, 7, 3, 1, -5],
    [8, 8, 0, 6, 0, 2, 4], 
    [5, 0, 3, 6, 7, 3, -3]
]

====>

[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0]
]
---------------------------
[
    [0, 5 ,6, 7, 3, 1, -5],
    [8, 8, 0, 6, 0, 2, 4], 
    [5, 5, 3, 6, 7, 3, -3]
]
rows = 0, 1
cols = 0, 2, 3

====>

[
    [0, 5 ,6, 7, 3, 1, -5],
    [8, 8, 0, 6, 0, 2, 4], 
    [5, 5, 3, 6, 7, 3, -3]
]

zeroes = [
    (0, 0), (1, 2), (1, 4)
]


1. Brute Force - Start with 0's, Try to Keep Elements

- make a MxN matrix of all zeroes
- check rows 
    - if the corresponding row in the input contains a 0, 
        leave the output as is
    - otherwise, copy over the row

2. Brute Force idea 2 --> can be in-place or out of place
    - record locations of all the 0s
    - iterate back over the array
        - if we hit one of those locations from before,
            "zeroify" that row and column
    - return the output


Edge Cases:
- empty array (check for that)
"""
from typing import List


def find_zeroes(matrix):
    rows, cols = set(), set()
    for row_ndx, row in enumerate(matrix):
        for col_ndx, element in enumerate(row):
            # only add the location if it's in a unique row and column
            if element == 0:
                if row_ndx not in rows:
                    rows.add(row_ndx)
                if col_ndx not in cols:
                    cols.add(col_ndx)
    return rows, cols


def zeroify_row(matrix, zero_row_ndx):
    # zeroify the matrix row
    for col_ndx in range(len(matrix[zero_row_ndx])):
        matrix[zero_row_ndx][col_ndx] = 0


def zeroify_col(matrix, zero_col_ndx):
    # zeroify the matrix column
    for row_ndx in range(len(matrix)):
        matrix[row_ndx][zero_col_ndx] = 0


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Input:

    [
           0  1  2  3  4  5   6
      > 0 [0, 0 ,0, 0, 0, 0, 0],
      > 1 [0, 8, 0, 6, 0, 2,  4], 
      > 2 [0, 5, 3, 6, 7, 3, -3]
    ]

    locations = [
        (0, 0), (1, 2), (1, 4), 
    ]

    ROW_LENGTH = 7
    rndx       row                      cndx    e
    0          [0, 5 ,6, 7, 3, 1, -5],  0       0
                                        1       5
                                        2       6
                                        3       7
                                        4       3
                                        5       1
                                        6      -5

    zrndx       cndx            zcndx    
    0           0                0
                1
                2
                3
                4
                5
                6

    Big O:
    Time: O(MxN)
    Space: O(M + N)


    Improvements: 
    - remember the rows and cols we've already marked for zeroifying:

    """
    # - record locations of all the rows and cols to zeroify
    rows, cols = find_zeroes(matrix)  # MxN iterations
    # - iterate back over the array
    # TODO: zeroify the rows
    for row_ndx in rows:  # M
        zeroify_row(matrix, row_ndx)  # N
    # TODO: zeroify the columns
    for col_ndx in cols:  # N
        zeroify_col(matrix, col_ndx)  # M
    """for zero_row, zero_col in zero_locations:   # MxN
        # "zeroify" that row and column 
        zeroify_row_col(matrix, zero_row, zero_col)  # M + N"""
    # - return the output
    return matrix
