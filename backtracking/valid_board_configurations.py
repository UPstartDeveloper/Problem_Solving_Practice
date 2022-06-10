from typing import Tuple


class Solution:
    """
    Suppose you are given a board with dimensions N by N.
    Given N, write a function that returns the number of possible arrangements 
    of the board where N queens can be placed on the board without threatening each other 
    (e.g. no 2 queens can share the same 
        row, 
        column, or 
        diagonal). 

    Input: 
        N: pos int < 10, immutable
           represents BOTH the side length of chess board, and 
                           # of queens for 1 config to be valid

    Out:
        int: # of valid configs
             each has N queens in the right pos
             and they just vary on where they are placed

    Intuition:
        - back tracking
        - DP
        - recursion
    
    EC:
        - N is not int - ValueError
        - N is out of range - ValueError
        - N <= 3 --> return 0

    """

    def valid_board_configurations(self, N: int) -> int:
        ### HELPERS

        def _traverse(row, col, board):
            # define 8 direction vectors
            directions = [
                (0, 1),  # down
                (1, 0),  # right
                (-1, 0),
                (0, -1),
                (1, 1),
                (-1, 1),
                (1, -1),
                (-1, -1),
            ]
            # traverse the grid in all 8 directions
            for delta_x, delta_y in directions:
                # TODO[test]: is it enough iterations?
                for _ in range(abs(len(board) - row)):
                    new_x, new_y = row + delta_x, col + delta_y
                    if -1 < new_x < len(board) and -1 < new_y < len(board[0]):
                        # fill in 1s
                        board[new_x][new_y] = 1
            # all done!

        def _place_queens(start_col: int) -> Tuple[Tuple[int, int]]:
            board = [[0 for _ in range(N)] for _ in range(N)]

            board[0][start_col] = 1
            _traverse(0, start_col, board)
            placed_queens = 1

            for row_index in range(len(N)):
                for col_index in range(len(N)):
                    # "is this available?" check
                    if board[row_index][col_index] == 0:
                        # traverse the grid to fill in spots
                        _traverse(row_index, col_index, board)
                        placed_queens += 1

            return placed_queens == N

        ### Check EC
        if isinstance(N, int) is False or not (0 < N < 10):
            raise ValueError(f"Expected pos int < 10 for arg N, received {N}.")
        elif N < 4:
            return 0

        ### DRIVER
        valid_configs = 0

        for start_col in range(N):
            # TODO[test] - by starting in a new col each time, we prevent dupe configs
            is_placement_valid = _place_queens(start_col)  # O(n^2)
            if is_placement_valid is True:
                valid_configs += 1

        return min(valid_configs, N)


### TODO: add test cases
