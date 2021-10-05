"""
Eight Queens: 

Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board 
so that none of them share the same 
row, 
column, or 
diagonal. 

In this case, "diagonal" means all diagonals, not just the two that bisect the board.

Test Input: n = 8

Output: none
StdOut:

"
    0   1   2   3   4   5   6   7
0   Q   X   X   X   X   X   X   X
1   X   X   X   Q   X   X   X   X
2   X   Q   X   X   X   X   X   X
3   X   X   X   X   Q   X   X   X
4   X   X   Q   X   X   X   X   X
5   X   X   X   X   X   Q   X   X
6   X   X   X   X   X   X   X   X
7   X   X   X   X   X   X   X   X

queens = 6, 5, 4, 3, 2

Clarifying Questions:
- how should the output look like? is the above ok?
    - numered rows and columns?
    - X marks where the queens are?
    - do we need to mark every cell that isn't filled by a queen/off-limits
    - and each board should start on a new line?
- no inputs?
- do all 8 queens needs to be on the board for it to count as a permutation?

Brainstorm:

1) DIY
queens = 8

choices --> the board
constraint --> the rules above, queens = 0 for it to be a solution
goal -->  get all the unique placements


- need to make sure that we follow the rules (maybe mark off the rows, cols, and diagonals?)
- need a way to make sure the arrangements that are printed are unique

Approach:
Base Case: queens == 0:
    return out the arrangement
    reset the board
    reset queens = 8
    call the function again
Recursive Case: queens > 0:
    - iterate over the rows and columns
        - place a Q on the first spot that's not X or B
        - check off the rows, columns, and diagonals
        - decrement queens
    - at end of the for loops
        - if the number of queens != 0 
            - it either means we need to stop - if there's a B in the second to last col
            - or it was just a bad placement - then reset the board
        - if it is, call the base case (print the board)

Helper Functions:
- check_off_row
    - same row, col ++
- check_off_col
    - row ++, same col
- check_off_diagonals
    - row ++, col ++
    - row --, col --
- reset_board:
    - remove the X's
    - replace the Q's in the first row w/ B's - "used before"

- how do we know when to stop?
    - guess it there should be enough 
"
"""

from typing import List


class Solution:

    output = list()

    def check_off_row(self, row_idx, board):
        # same row, col ++
        for col_idx in range(len(board[row_idx])):
            board[row_idx][col_idx] = "X"
        return

    def check_off_col(self, col_idx, board):
        # row ++, same col
        for row_idx in len(board):
            board[row_idx][col_idx] = "X"
        return

    def check_off_diagonals(self, row_idx, col_idx, board):
        def find_diagonal_above(is_left):
            start_row, start_col = row_idx, col_idx
            """find the starting point for the diagonal from above"""
            if is_left is True:
                while start_col > -1:
                    start_col -= 1
                    start_row -= 1
            else:  # on the latter half of the cols
                while start_col < len(board[0]):
                    start_col += 1
                    start_row -= 1
            return start_row, start_col

        def find_diagonal_below(is_left):
            """find the starting point of the diagonal from below"""
            start_row, start_col = row_idx, col_idx
            if is_left is True:
                while start_col > -1:
                    start_col -= 1
                    start_row += 1
            else:  # on the latter half of the cols
                while start_col < len(board[0]):
                    start_col += 1
                    start_row += 1
            return start_row, start_col

        def check_downwards(start_row, start_col, is_left):
            """check off all spaces in the diagonal (go downwards); row ++, col++"""
            if is_left is True:
                # left to right
                while start_col < len(board) and start_row < len(board):
                    board[start_row][start_col] = "X"
                    start_row += 1
                    start_col += 1
            else:  # right to left
                while start_col > -1 and start_row < len(board):
                    board[start_row][start_col] = "X"
                    start_row += 1
                    start_col -= 1

        def check_upwards(start_row, start_col, is_left):
            """check off all spaces in the diagonal (go upwards); row --, col++"""
            if is_left is True:
                # left to right
                while start_col < len(board) and start_row > -1:
                    board[start_row][start_col] = "X"
                    start_row -= 1
                    start_col += 1
            else:  # right to left
                while start_col > -1 and start_row > -1:
                    board[start_row][start_col] = "X"
                    start_row -= 1
                    start_col -= 1

        # determine which side we're on
        is_left = True
        if col_idx >= len(board) // 2:
            is_left = False
        # check off the diagonal from below first
        start_row, start_col = find_diagonal_below(is_left)
        check_upwards(start_row, start_col, is_left)
        # check off the diagonal from above next
        start_row, start_col = find_diagonal_above(is_left)
        check_downwards(start_row, start_col, is_left)
        return

    def reset_board(self, n, board):
        # replace the the X's and B's w/ periods
        b_locs = list()
        for row_idx, row in enumerate(board):
            for col_idx, char in enumerate(row):
                if char == "X" or char == "B":
                    row[col_idx] = "."
                    # if it was a B, save it for later
                    if char == "B":
                        b_locs.append((row_idx, col_idx))
        # add the board to the output, if n == 0
        if n == 0:
            self.output.append(board)
        # replace the Q's in the first row w/ B's - "used before"
        for col_idx, char in enumerate(board[0]):
            if char == "Q":
                board[0][col_idx] = "B"
        # restore the "B"'s that were there before
        index_bs = 0
        for row_idx, row in enumerate(board):
            for col_idx, char in enumerate(row):
                if index_bs < len(b_locs) and (row_idx, col_idx) == b_locs[index_bs]:
                    board[row_idx][col_idx] = "B"
                    index_bs += 1
        return

    def solveNQueens(self, n: int, board=None) -> List[List[str]]:
        while True:
            # A: get the number of queens and the board
            if board is None:
                board = ["".join(["." for _ in range(n)]) for _ in range(n)]
            # B: iterate over the rows and columns to solve the board
            for row_idx, row in enumerate(board):
                for col_idx, char in enumerate(row):
                    # place a Q on the first spot that's not "."" or B
                    if char != "." and char != "B":
                        row[col_idx] = "Q"
                        # check off the rows, columns, and diagonals
                        self.check_off_row(row_idx, board)
                        self.check_off_col(col_idx, board)
                        self.check_off_diagonals(row_idx, col_idx, board)
                        # decrement queens
                        n -= 1
            # C: at end of the for loops, try to see if we solved it
            if n != 0:
                # we may need to STOP - there's a B in the 2nd to last col
                if board[0][n - 2] == "B":
                    return self.output
                else:  # or it was just a bad placement - then reset the board
                    self.reset_board(n, board)
            # D: if we solved the board, then reset it
            else:  # n == 0
                self.reset_board(n, board)
