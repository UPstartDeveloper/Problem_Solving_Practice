def spiral_copy(inputMatrix):
    """
    Returns the elements of a 2D array in clockwise order.

    Parameters:
    inputMatrix: List[List[int]]

    Returns: List[int]


                        ^ row index (moving through a col)
                        |
                        |
                        |
                        |                  col index (moving across a row) +
        <---------------------------------->
                        |
                        |
                        |
                        |
                        v


    """
    # define direction that the snake goes in, and its limits
    RIGHT, DOWN, LEFT, UP = ((0, 1), (1, 0), (0, -1), (-1, 0))
    # numbers for the rows and columns we have yet to traverse
    col_limit = len(inputMatrix[0]) - 1  # 4, 3, 2  # O(c)
    row_limit = len(inputMatrix) - 1  # 4 3   O(r)
    current_limit = (0, col_limit)
    # start at top
    current_position = (0, 0)
    # init direction the snake travels
    direction = RIGHT
    # init return list
    elements = list()  # []   int[] ouput = new int[]
    # calculate the stop condition = # of elements to add
    NUM_ELEM = 0
    # O(n)
    for row in inputMatrix:
        NUM_ELEM += len(row)
    # start spiraling
    while len(elements) < NUM_ELEM:  # n iterations
        # getting the element at the position we're currently at
        row_position, col_position = current_position
        element = inputMatrix[row_position][col_position]
        # add the element to the list
        elements.append(element)
        # if needed, change the direction
        if current_position == current_limit:
            current_limit_row, current_limit_col = current_limit
            # change to the appropiate direction, and the appropiate limit
            if direction == RIGHT:
                # change the direction
                direction = DOWN
                # change the limit
                current_limit = (current_limit_row + row_limit, current_limit_col)
            elif direction == DOWN:
                # change the direction
                direction = LEFT
                # change the limit
                current_limit = (current_limit_row, current_limit_col - col_limit)
            elif direction == LEFT:
                # change the direction
                direction = UP
                # change the limit
                current_limit = (current_limit_row - row_limit, current_limit_col)
            elif direction == UP:
                # change the direction
                direction = RIGHT
                # change the limit
                current_limit = (current_limit_row, current_limit_col + col_limit)
            # if we moved from a horizontal to a vertical direction
            if direction == DOWN or direction == UP:
                # remove the row just traversed, from the constraints of our box
                row_limit -= 1
            # if we moved from a vertical to horizontal direction
            elif direction == LEFT or direction == RIGHT:
                # remove the column just traversed, from the constraints of our box
                col_limit -= 1
        # resolve the direction vector into its individual components
        change_in_row, change_in_col = direction
        # change the position, move one step in the direction we're currently in
        current_position = (row_position + change_in_row, col_position + change_in_col)
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
