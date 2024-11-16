class Solution:
    """https://neetcode.io/problems/search-for-word"""
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        Intuition:
            graph traversal - DFS? if not, BFS

        Edge Cases
            - empty grid --> N/A
            - empty string --> N/A
            - jagged grid ---> might not be an issue, if we check for index out of bound errors?

        Constraints
            graph = rectangular 2D list
            at most 5x5 cells
            cell = node
            edges = 4 cardinal directions
            case-sensitive
            ASSUME:
                grid is immutable - once visited, put coords in a set so we don't revist

        Goal:
            path-finding in order to spell a string
            return bool

        BCR:
            O(r * c) - at worst, we have to visit all cells at least 1x

        Approaches

            1) Non-mutating DFS:

                A: init output is_word_found = False

                B: maintain current_letter_index = 0

                C: enter nested loop traversal over grid

                    when cell_letter == first word letter --> begin dfs
                        ... # TODO[dfs]
                        init a stack = []
                        init a visited set = {}
                        add current coords to visited
                        push neighbors of first word letter
                            check if their coords are in bounds
                            and check if their letter == letter of word[current_index + 1]
                            and check their coords not in visit
                        while stack:
                            coords, word_index = stack.pop()
                            check for coords not in visited:
                                add coords to visited
                                if word_index == len(word)
                                    we're done! --> set is_word_found = True, exit early
                                push neighbors
                                    check if their coords are in bounds
                                    and check if their letter == letter of word[current_index + 1]
                                    and check their coords not in visit

                    if dfs finds word ---> is_word_found = True, exit early
                    else - reset stack and visited

                D: return is_word_found

            Tests:
                is_word_found = False
                current_letter_index = 0
                row_i   col_i
                0       0
                        1

                visited = {(0, 1)}
                stack
                [(1, 1, 1)]

        """
        ### HELPER(S)
        def _is_word_end_found(coords, word_index, visited):
            # check for coords not in visited:
            if coords not in visited:
                # add coords to visited
                visited.add(coords)
                row, col = coords
                if word_index == len(word) - 1 and word[word_index] == board[row][col]:
                    return True
                elif word[word_index] == board[row][col]:
                    # push neighbors
                    for neighbor_row, neighbor_col in [
                        (row - 1, col),  # up
                        (row, col + 1),  # right
                        (row + 1, col),  # down
                        (row, col - 1),  # left
                    ]:
                        nr = neighbor_row
                        nc = neighbor_col
                        if -1 < nr < len(board):
                            if -1 < nc < len(board[nr]):
                                if (nr, nc) not in visited:
                                    if ((word_index + 1 == len(word)) or (word[word_index + 1] == board[nr][nc])):
                                        if _is_word_end_found((nr, nc), word_index + 1, visited.copy()):
                                            return True
            return False

        ### DRIVER
        # A: init output
        is_word_found = False
        grid = board
        # B: enter nested loop traversal over grid
        for row_index in range(len(grid)):
            num_cols = len(grid[row_index])
            for col_index in range(num_cols):
                # when cell_letter == first word letter --> begin dfs
                if grid[row_index][col_index] == word[0]:
                    is_word_found = _is_word_end_found(
                        (row_index, col_index),
                        0,
                        set()
                    )
                    # if dfs finds word ---> is_word_found = True, exit early
                    if is_word_found:
                        return True
        # C: end of algo
        return is_word_found

"""
board = [

  ["A","B","C","D"],

  ["S","A","A","T"],
                    ^
  ["A","C","A","E"]
                        ^
],

is_word_found = F,

word = "BAT"
        ^

ri = 0
ci = 0, 1




                        (0, 0)         1.       {(0, 1)} ---> False
                        (1, 1)         1.       {(0, 1)} ---> False
                        (0, 1)         0.       {}
_is_word_end_found.    coords.      word_i,      v --> False
"""
