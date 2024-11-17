class Solution:
    """https://neetcode.io/problems/count-paths"""
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Input(s):
            m = rows of a grid
            n = cols of the grid

        Output
            int - num of possible paths

        EC:
            N/A -- m and n both pos int

        BCR - ???

        Intuition
            backtracking - use DFS to count up all possible paths

        Approach
            node = cell
            edges = down and to the right

            1. Graph DFS - or perhaps a tree

            2. DP table
                recurrence relations
                    # of paths from a cell = sum(paths from below + to the right)

                A: init the table
                B: fill in ans for base cases
                    - bottom right = 0
                    - last col = 1
                    - last row = 1

                C: fill in the rest - traverse the table right to left, bottoms up
                D: return value in top-left cell
        """
        ### DRIVER

        # A: init the DP table
        grid = [[0 for _ in range(n)] for _ in range(m)]

        # B: fill in base cases
        grid[-1][-1] = 0
        for row_index in range(m):
            grid[row_index][-1] = 1
        for col_index in range(n):
            grid[-1][col_index] = 1

        # C: fill in the rest
        for row_index in range(m - 2, -1, -1):
            for col_index in range(n - 2, -1, -1):
                grid[row_index][col_index] = (
                    grid[row_index + 1][col_index]
                    + grid[row_index][col_index + 1]
                )

        # D: return answer
        return grid[0][0]
