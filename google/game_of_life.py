from typing import List


class Solution:
    DIRECTIONS = [
        (0, -1),  # left
        (0, 1),  # right
        (1, 0),  # down
        (-1, 0),  # up
        (1, -1),  # bottom left
        (1, 1),  # bottom right
        (-1, -1),  # up left
        (-1, 1),  # up right
    ]

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Leetcode: https://leetcode.com/problems/game-of-life/
        
        Do not return anything, modify board in-place instead.
        
        Input/Problem:
            2D array - binary int, mutable, guaranteed not empty, 
            1 = live
            0 = dead
            
        
        """
        ### HELPER
        def _invert_bit(row_index, col_index):
            """1 --> 0, and 0 --> 1"""
            bit = board[row_index][col_index]
            board[row_index][col_index] = bit ^ 1

        def _count_live_neighbor(row_index, col_index):
            """TODO: traverse the 8 directions, see which is live"""
            count = 0
            for row_change, col_change in self.DIRECTIONS:
                neighbor_row = nr = row_index + row_change
                neighbor_col = nc = col_index + col_change
                # watch for IndexError
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] == 1:
                        count += 1
            return count

        def _needs_change(row_index, col_index) -> bool:
            # A: current state?
            state = board[row_index][col_index]
            # B: TODO: # of live neighbors?
            num_live = _count_live_neighbor(row_index, col_index)
            # C: evaulate the appropiate
            if state == 1 and (num_live < 2 or num_live > 3):
                return True
            elif state == 0 and num_live == 3:
                return True
            # needs no change
            return False

        ### MAIN
        # A: init a set of coords
        coords = set()
        # B: eval which coords need to change state
        for row_index in range(len(board)):
            row = board[row_index]
            for col_index in range(len(row)):
                # save it in the set
                if _needs_change(row_index, col_index) is True:
                    coords.add((row_index, col_index))
        # C: apply the changes
        for row_index, col_index in coords:
            _invert_bit(row_index, col_index)
