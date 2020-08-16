"""
This is the "Rotate Image" problem on Leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770
"""

# Out of Place Solution
def rotate_out_of_place(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    """
    Idea #1: Swaps
    
    A: moving the upper left corner over to the right spot [0, len(maxtrix[0]) - 1]
    B: move the other elements one element up
    0,0, 0,1, 0,2
    [1,2,3],      [1, 0, 0]
    [4,5,6],  ->   0, 0, 0
    [7,8,9]       0, 0, 0
    

    
    """
    NUMCOLS = len(matrix[0])
    NUMROWS = len(matrix)
    # initialize the 2d matrix
    new_matrix = [[0 for i in range(NUMCOLS)] for j in range(NUMROWS)]
    # populate the cols in the new matrix, with rows from the original
    for index_row, row in enumerate(matrix):
        for index_col, value, in enumerate(row):
            # calculate the shared column
            new_col = NUMROWS - (index_row + 1)
            # calculating the new row
            new_row = index_col
            new_matrix[new_row][new_col] = value
    print(new_matrix)
    matrix = new_matrix
    return matrix
        