class Solution:
    POS_VAL = "O"
    NEG_VAL = "X"

    def solve(self, board: List[List[str]]) -> None:
        """
        Leetcode Link: https://leetcode.com/problems/surrounded-regions/
        Do not return anything, modify board in-place instead.

        Input/Problem:
             - ASSUME non-empty input
             - binary ==> X/O
             - region:
                - 4 direction= U/D/L/R
                - region = set of connected comps in the graph
                - vertex = cell that's an O
                    - data = X/O
                    - edges = LR/UD


            [xxxxxxxxxxxxxxxxx]
            [xxxxxxxxxoxxxxxxx]
            [xxxxxxxxoxoxxxxxx]

        EC:
            1) Invalid Input data --> ValueError?
                - non binary board
                - empty board
            2) TODO

        Intuition:
            undirected graph
            region = set of connected comps in the graph

        Approach:

            1) DFS:
                A: traverse the board
                    B: find a region - decide if we can modify it
                        B1: DFS -- to try and reach the end --> save coords in a set
                        C: if we cannot reach --> modify the the cells
                D: return the board in place

        """
        ### HELPERS
        def _get_neighbors(row, col):
            DIRECTIONS = [
                (0, 1),  # down
                (0, -1),  # up
                (1, 0),  # right
                (-1, 0),  # left
            ]
            possible_coords = [
                (row + change_in_row, col + change_in_col)
                for change_in_row, change_in_col in DIRECTIONS
            ]
            # check if they're in bounds, and == 'O'
            neighbors = list()
            for pr, pc in possible_coords:
                if 0 <= pr < len(board) and 0 <= pc < len(board[0]):
                    if board[pr][pc] == self.POS_VAL:
                        neighbors.append((pr, pc))
            return neighbors

        def _is_surrounded(row_index, col_index, globally_visited):
            """iterative DFS"""
            locally_visited, stack = set(), list([(row_index, col_index)])
            is_surrounded = True
            # A: DFS the region
            while stack:
                # pop a node
                current_row, current_col = stack.pop()
                cr = current_row
                cc = current_col
                # C: decide if this region is surrounded
                if (
                    cr == 0
                    or cr == len(board) - 1
                    or cc == 0
                    or cc == len(board[0]) - 1
                ):
                    is_surrounded = False
                locally_visited.add((current_row, current_col))
                # push on the neighboring nodes
                neighbors = _get_neighbors(current_row, current_col)
                for n in neighbors:
                    nr, nc = n
                    if (nr, nc) not in locally_visited:
                        stack.append(n)
            # B: prevent re-visiting
            for coords in locally_visited:
                globally_visited.add(coords)
            # D: return!!!
            return is_surrounded, locally_visited

        def _capture_region(coords):
            """we cannot reach --> modify the the cells"""
            for row, col in coords:
                if 0 <= row < len(board) and 0 <= col < len(board[0]):
                    board[row][col] = self.NEG_VAL

        ### DRIVER
        # A: traverse the board
        globally_visited = set()
        # B: find a region
        for row_index, row in enumerate(board):
            for col_index, elem in enumerate(row):
                is_unvisited = (row_index, col_index) not in globally_visited
                if elem == self.POS_VAL and is_unvisited:
                    # decide if we can modify it, save coords in a set - DFS
                    can_modify, coords = _is_surrounded(
                        row_index, col_index, globally_visited
                    )
                    if can_modify:
                        _capture_region(coords)
                else:  # it's an X
                    globally_visited.add((row_index, col_index))
        # D: return the board in place
        return board
