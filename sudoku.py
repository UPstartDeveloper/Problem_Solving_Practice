def validate_sudoku_board(board):
    def validate(values, values_set):
        # make sure there are no duplicates or 0's
        print(f'Comparing {values_set}, to {values}')
        if "0" not in values_set and len(values_set) == len(values):
            return True
        return False
    is_valid = True
    # A: validate rows
    for row in board:  # 9 iterations
        # make a set of the row
        row_values = [value for value in row if value != "."]  # 9 iterations
        row_set = set(row_values)
        # validate
        is_valid = validate(row_values, row_set)
        if is_valid is False:
            # print("row invalid")
            return is_valid
    # B: validate columns:
    for col_index, value in enumerate(board[0]):
        # validate the values in each column
        column = list()
        for row in board:
            value = row[col_index]
            if not value == ".":
              column.append(value)
        # make a set of the column
        col_set = set(column)
        # validate
        is_valid = validate(column, col_set)
        if is_valid is False:
            # print("column invalid")
            return is_valid
    # C: validate the sub-boxes - iterate left to right, top down
    start_row, end_row = 0, 3
    while end_row < len(board) + 1:
        # set indices for columns
        row = board[start_row]
        start_col, end_col = 0, 3
        # validate one row of sub-boxes
        while end_col < len(row) + 1:
            box_values = list()
            # collect values in one box
            for row_index in range(start_row, end_row):
              for col_index in range(start_col, end_col):
                # print("adding coordinates", row_index, col_index)
                value = board[row_index][col_index]
                if not value == ".":
                  box_values.append(value)
            # validate the one box
            box_set = set(box_values)
            # validate
            is_valid = validate(box_values, box_set)
            if is_valid is False:
              return is_valid
            # move on to the next box, in same row of sub-boxes
            start_col += 3
            end_col += 3
            # move on to the next row of sub-boxes
            start_row += 3
            end_row += 3
    # D: otherwise the board is valid
    return is_valid
  
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(validate_sudoku_board(board))

"""
Things to Keep in Mind About This Problem

- in my approach, you need to watch out for the number of times "." appears
- optimization lies mostly in space, not time as the input doesn't increase

"""