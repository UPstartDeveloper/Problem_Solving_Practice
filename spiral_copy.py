def spiral_copy(inputMatrix):
    """
    are we guaranteed to have a rectangular matrix? - yes
    I assume we have at inner array

    Idea #1:

    define direction that the snake - O(1)
    - right = (0, +1), limit: last column
    - down = (+1, 0), limit: last row
    - left = (0, -1), limit: first column
    - up = (-1, 0), limit: first row
    limit_directions = {
        4: right,
        4: down,
        0: left,
        0: up
        }

    start at top (first element of the first array) 
    init current_position = (0, 0
    init direction as right - O(1)
    init an empty 1D array to return at  - O(1)
    calculate the number of elements in the 2D  - O(n)

    init direction variable = right


    while the list hasn't gotten all the elements and whatever direction we're hasn't reached it's limit:
    # get the number at the position
    # add it to the 1D
    # if needed, we'll change the direction
        - if you change the direction to down:
        - move down the limit for the "up direction"
        up_limit = 0, 1, 2
        - if you change the direction to left:
        - move left the limit for the "right direction"
        


    return the list
    """
    # define direction that the snake goes in, and its limits
    right, down, left, up = (
        (0, 1), (1, 0), (0, -1), (-1, 0)
    )
    # numbers for the rows and columns we have yet to traverse
    col_limit = len(inputMatrix[0]) - 1  # 4, 3, 2
    row_limit = len(inputMatrix) - 1  # 4 3
    # map the directions to their limits
    """direction_limits = {
        right: (0, NUM_COLS),
        down: (NUM_ROWS,
        left: 0,
        up: 0
        }
    """
    current_limit = (0, col_limit)
    # start at top 
    current_position = (0, 0)
    # init direction the snake travels 
    direction = right
    # init return list
    elements = list()
    # calculate the stop condition = # of elements to add
    NUM_ELEM = 0
    for row in inputMatrix:
        NUM_ELEM += len(row)
    # start spiraling
    while len(elements) < NUM_ELEM:
        # getting the element at the position we're currently at
        row_position, col_position = current_position
        element = inputMatrix[row_position][col_position]
        # add the element to the list
        elements.append(element)
        # if needed, change the direction
        if current_position == current_limit:
            current_limit_row, current_limit_col = current_limit
            # change to the appropiate direction
            if direction == right:
                direction = down
                # change the limit 
                current_limit = (
                    current_limit_row + row_limit , 
                    current_limit_col
                )
            elif direction == down:
                direction = left
                current_limit = (
                    current_limit_row, 
                    current_limit_col  - col_limit
                )
                # remove the row just traversed, from the constraints of our box
                # col_limit -= 1
            elif direction == left:
                direction = up
                current_limit = (
                    current_limit_row - row_limit, 
                    current_limit_col
                )
            # move up the down limit
            elif direction == up:
                direction = right
                current_limit = (
                    current_limit_row, 
                    current_limit_col + col_limit
                )
            # change the limits, based on the direction we went to
            # if we moved from a horizontal to a vertical direction
            if direction == down or direction == up:
                # remove the row just traversed, from the constraints of our box
                row_limit -= 1
            # if we moved from a vertical to horizontal direction
            elif direction == left or direction == right:
                col_limit -= 1
        # change the position in the direction we're currently in
        # resolve the direction vector into its individual components
        change_in_row, change_in_col = direction
        current_position = (
            row_position + change_in_row,
            col_position + change_in_col
        )
        print(elements)
        print(f'Position {current_position}, Limit: {current_limit}')
        print(f'Limits row and col: {row_limit, col_limit}')
    return elements

"""
current_limit

(0, 4)  # initial state
(4, 4)  # first down direction change
(4, 0)  # moving left
(1, 0)  # moving up


inputMatrix  = [ 
[1,    2,   3,  4,    5],
[6,    7,   8,  9,    10],
[11,    12,  13,  14,  15],
[16,    17,  18,  19,  20] 
]

right,   down,   left,    up = (
(0, 1), (1, 0), (0, -1), (-1, 0)
)

NUM_ELEM = 20

col_limit | row_limit | current_limit | current_position  | direction   |   elements  
2       |    0     |  (2, 1)       |   (2, 1)         |   (0, -1)    | [1, 2, 3, 4, 5,
                                                                        10, 15, 20, 19, 18,
                                                                        17, 16, 11, 6,  7,
                                                                        8,  9,  14, 13, 12
                                                                        ]

current_limit_row = 1
current_limit_col = 3
change_in_row = 0
change_in_col = -1
"""

if __name__ == "__main__":
    inputMatrix  = [ [1,    2,   3,  4,    5],
                     [6,    7,   8,  9,   10],
                     [11,  12,  13,  14,  15],
                     [16,  17,  18,  19,  20] ]
    print(spiral_copy(inputMatrix))