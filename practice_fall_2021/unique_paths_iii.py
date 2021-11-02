from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        Leetcode Link: https://leetcode.com/problems/unique-paths-iii/

        Input/Problem:
            - input is immutable
            - 4 cardinal dirs - 1 step at a time
            - find the # of paths
                - 1 ---> 2
                    - only over the 0 squares
                    - all the 0 sqaures
                    - 4 directions
            - ASSUME grid is not empty, it can fit one machine
            - ASSUME >= 1 path between 1 and 2

        EC:
            1) jagged grid?
            2) invalid intger ---> ValueError
            3) TODO

        Intution:
            backtracking problem
            graph
                - directional (no revisiting cells)
                - edges = 4 cardinal directions
                - vertices = cells thwmselves

        Approach:
            1) Brute Force:
                1) DFS to get all the unique paths between 1 and 2
                2) subset - paths that went over all the un-obs cells
                3) return the number of those paths
        """
        ### HELPERS
        def _get_neighbors(coords, path_so_far):
            # A: get coords of potential neighbors
            cr, cc = coords
            neighbors = [
                (cr, cc + 1),  # right
                (cr, cc - 1),  # left
                (cr + 1, cc),  # down
                (cr - 1, cc),  # up
            ]
            # B: subset: in bounds
            in_bounds = [
                (nr, nc)
                for nr, nc in neighbors
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0])
            ]
            # C: subset: not yet visited
            return [(nr, nc) for nr, nc in in_bounds if (nr, nc) not in path_so_far]

        def _search_for_paths(coords, path_so_far, all_paths):
            # A: visit the current node
            path_so_far.append(coords)
            current_row = cr = coords[0]
            current_col = cc = coords[1]
            # B: Base Case: destination has been found!
            if grid[cr][cc] == 2:
                all_paths.add(tuple(path_so_far.copy()))
            # C: Recurse on the neighbors
            elif grid[cr][cc] == 0 or grid[cr][cc] == 1:
                neighbors = _get_neighbors(coords, path_so_far)
                for nr, nc in neighbors:
                    if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        _search_for_paths((nr, nc), path_so_far, all_paths)
            # D: remove the node added
            path_so_far.remove(coords)
            return all_paths

        def _find_all_paths(grid):
            """Recursive DFS solution to find all the paths"""
            # A: TODO[refactor-shorten] start by getting starting cell
            start_row = sr = 0
            start_col = sc = 0
            while sr < len(grid):
                row, sc = grid[sr], 0
                while sc < len(row) and grid[sr][sc] != 1:
                    sc += 1
                # if found 1: stop!
                if sc < len(grid[0]):
                    break
                # move on to the next row
                else:
                    sr += 1
            # B: init a set of paths fromm start to finish
            all_paths = _search_for_paths((sr, sc), list(), set())
            # C: DFS to find the paths
            return all_paths

        def _subset(all_paths):
            """Measure all the paths that are as long == # of 0's"""
            # A: count all un-obs cells
            required_len = 2
            for row in grid:
                for elem in row:
                    if elem == 0:
                        required_len += 1
            # B: get the paths that have the right number of steps
            return [p for p in all_paths if len(p) == required_len]

        ### DRIVER
        # 1) DFS to get all the unique paths between 1 and 2
        all_paths = _find_all_paths(grid)
        # 2) subset - paths that went over all the un-obs cells
        all_desired_paths = _subset(all_paths)
        # 3) return the number of those paths
        return len(all_desired_paths)
