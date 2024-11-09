class Solution:
    """https://neetcode.io/problems/count-number-of-islands"""
    def num_islands(self, grid: list[list[str]]) -> int:
        """
        Intuition:
            graph traversal
                nodes = 1's
                edges - 4 cardinal directions

        Constraints
            land only in the grid
            grid not empty
            grid is rectangular
            is grid mutable?? ---> yes
            grid is "binary"

        Approach:

            1) DFS

                START: init island_count = 0

                A: traverse grid

                    i: if land found, save current (row, col),
                        and start a search (DFS)
                    ii: init a stack, push the first land
                    iii: "visit" each land in the stack
                        a. pop the land (row,col)
                        b. mark it as water
                        c. check if it's 4 neighbors are land - if so, push them onto the stack
                    iv. when stack is empty --> increment island count
                    v. resume grid traversal from last saved (row, col)


                END: reutrn island_count

                Time: O(r * c)
                Space: O(r * c)

        grid
              v
            ["0","0","0","0","1"],
            ["0","0","0","0","1"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]

        island_count (ic)
        0

        cr
        0

        cc
        0

        stack = [
            (1, 0),

        ]

        nlrp
        0

        nlcp
        0
        """
        ### HELPERS
        def _dfs(row, col) -> None:
            """iterative DFS tuses a regular list for a stack - list.append and list.pop"""
            # ii: init a stack, push the first land
            stack = list([(row, col)])
            # iii: "visit" each land in the stack
            while len(stack) > 0:
                # a. pop the land (row,col)
                next_land_row_pos, next_land_col_pos = stack.pop()
                # b. visit it - but only if needed
                if grid[next_land_row_pos][next_land_col_pos] == "1":
                    # mark it as water
                    grid[next_land_row_pos][next_land_col_pos] = "0"
                    # push the neighbors onto the stack
                    for next_cell_coords in [
                        (next_land_row_pos + 1, next_land_col_pos),  # down
                        (next_land_row_pos -1, next_land_col_pos),  # up
                        (next_land_row_pos, next_land_col_pos - 1),  # left
                        (next_land_row_pos, next_land_col_pos + 1),  # right
                    ]:
                        next_row = next_cell_coords[0]
                        next_col = next_cell_coords[1]

                        if -1 < next_row < len(grid):
                            if -1 < next_col < len(grid[0]):
                                # c. check if the neighbor is land - if so, push them onto the stack
                                if grid[next_cell_coords[0]][next_cell_coords[1]] == "1":
                                    stack.append(next_cell_coords)

        ### DRIVER
        # START: init island_count = 0
        island_count = 0

        # A: traverse grid
        current_row = 0

        while current_row < len(grid):

            current_col = 0
            while current_col < len(grid[0]):

                # i: if land found, save current (row, col)
                current_cell = grid[current_row][current_col]

                if current_cell == "1":
                    # start a search (DFS)
                    _dfs(current_row, current_col)  # modifies the grid
                    # iv. when stack is empty --> increment island count
                    island_count += 1

                # v. resume grid traversal from last saved (row, col)
                current_col += 1

            current_row += 1

        # all done
        return island_count
