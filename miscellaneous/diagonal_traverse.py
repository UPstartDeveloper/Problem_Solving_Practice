from typing import List


def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    """
    not necessarily a rectanngle
    at least 1 row
    size of row <= 1

    [

    [1,2,3],
    [4,5,6],
    [7,8,9]

    ]

    r =   0, 1, 0, 2, 1, 0, 2, 1
    c =   0, 0, 1, 0, 1, 2, 1, 2
    num = 1, 4, 2, 7, 5, 3, 8, 6

    for each diagonal
        count down the row, index
        count up the col index

    tip = up + right
    tail = down + right
    row = count down
    col = count up

    Idea #1

    - # of vectors we need
    - init a list
    - iterate over all the vector
        - tail (starting pt)
        - tip (ending pt)
        iterate over all the values in between
            - row-=1
            - col+=1
            - add them to our list
    - return
    """
    """# define the directions
    UP, DOWN, RIGHT = [
        (-1, 0),
        (1, 0),
        (0, 1),
        
        
    change: we cannot assume that the longest row is at the bottom is
            the last row
    ]"""
    """
    # # of vectors we need
    NUM_VECTORS = len(nums) + len(nums[-1]) - 1
    # init a list 
    output = list()
    # initialize the starting row and col indicies
    NUM_FIRST_COL_VECTORS = len(nums)
    NUM_LAST_ROW_VECTORS = NUM_VECTORS - NUM_FIRST_COL_VECTORS
    COL_LIMIT = len(nums[-1])
    # iterate over all the vector
    starting_row = 0
    starting_col = 0
    starting_row_limit = 0
    for vector_iterator in range(NUM_VECTORS): # NV iterations
        # calc tail (starting pt)
        if vector_iterator < NUM_FIRST_COL_VECTORS:
            # start in the first col
            col = 0
            # start in a lower row than before
            row = starting_row
            # go up to the first row 
            row_limit = -1
        else: 
            # start in a col greater than the one before
            col = starting_col
            # start the last row
            row = len(nums) - 1
            # go up 1 less than the previous row limit
            row_limit = starting_row_limit
        # calc tip - iterate over all the values in between
        while row > -1:
            # add the next element to our list
            try:
                output.append(nums[row][col])
            except IndexError:
                pass
            # update the indices
            row -= 1
            col += 1
        # increment the starting row 
        if vector_iterator < NUM_FIRST_COL_VECTORS - 1:
            starting_row += 1
        else:  # last row vector - increment starting col
            starting_col += 1
            starting_row_limit += 1
    # return the list
    return output

    # O(nums) - time + space 
    """
    # get the longest row index, and calculate the size of nums
    size, longest_row_length, longest_row_index = 0, 0, 0
    for row_index, row in enumerate(nums):
        if len(row) > longest_row_length:
            longest_row_length = len(row)
            longest_row_index = row_index
        size += len(row)
    # find the indices of the final tail we want to traverse from
    FINAL_COL = len(nums[longest_row_index]) - 1
    FINAL_ROW = longest_row_index
    # init the starting row and column
    starting_row, starting_col = 0, 0
    # init the output list
    output = list()
    # iterate over each of the diagonals
    while len(output) < size:
        row = starting_row
        col = starting_col
        # add the values in that diagonal to our output
        while row > -1:
            # add the next element to our list
            try:
                output.append(nums[row][col])
            except IndexError:
                pass
            # update the indices
            row -= 1
            col += 1
            print(output, row, col)
        # update the starting row and column to find the next tail
        if starting_row < FINAL_ROW:  # moving down the first column
            starting_row += 1
        # moving across the last row
        elif (
            starting_row == FINAL_ROW or starting_row == longest_row_index
        ) and starting_col < len(nums[starting_row]):
            starting_col += 1
        # when the last row is not one of the longest length
        elif starting_col < FINAL_COL:
            starting_row -= 1
            starting_col += 1
        """
        [
            [2,2,2,2],
            [2],
            [2,2,2,2,2,2,2,2,2,22,2,2]
            [2,2,2,2]
        ]
        """
    # return the final list
    return output


"""

    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
NUM_VECTORS = 3 + 3 - 1 = 5
NUM_FIRST_COL_VECTORS = 3
ROW_LIMIT = 3
NUM_LAST_ROW_VECTORS = 2
COL_LIMIT = 3

    output = [1, 4, 2, 7, 5, 3, 8, 6]

sr      sc      vi         c    r   
2       1       2          3    -1











[
[1,2,3,4,5],
[6,7],
[8],
[9,10,11],
[12,13,14,15,16]
]

NUM_VECTORS = 5 + 5 - 1 = 9
NUM_FIRST_COL_VECTORS = 5
ROW_LIMIT = 5 
NUM_LAST_ROW_VECTORS = 2
COL_LIMIT = 3

    output = [1, ]

sr      sc      vi         c    r   
0       0       0          1    2


[
    [14,12,19,16,9],
    [13,14,15,8,11],
    [11,13,1]. 
--------------------------------------

Idea: elements at the same sum index belong in the same diagonal
    - start at 0,0 - always guaranteed to be there
    - start the next diagonal
        - always go down if we can
        - then we go right if there more elements in our row
        - if we run out of elements in the bottom, go to the largest 
            row (if any)

"""

if __name__ == "__main__":
    # test cases - sqaure
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert findDiagonalOrder(nums) == [1, 4, 2, 7, 5, 3, 8, 6, 9]
    nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    assert findDiagonalOrder(nums) == [
        1,
        6,
        2,
        8,
        7,
        3,
        9,
        4,
        12,
        10,
        5,
        13,
        11,
        14,
        15,
        16,
    ]
    nums = [[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]
    assert findDiagonalOrder(nums) == [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11]
    nums = [[1, 2, 3, 4, 5, 6]]
    assert findDiagonalOrder(nums) == [1, 2, 3, 4, 5, 6]
    nums = [[14, 12, 19, 16, 9], [13, 14, 15, 8, 11], [11, 13, 1]]
    assert findDiagonalOrder(nums) == [14, 13, 12, 11, 14, 19, 13, 15, 16, 1, 8, 9]
