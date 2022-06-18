from typing import List


class Solution:
    """
    LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/

    There is an m x n rectangular island that borders both the Pacific Ocean 
    and Atlantic Ocean. (pretty big huh?)
    
    The Pacific Ocean touches the island's left and top edges, 
    and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. 
    You are given an m x n integer matrix heights where 
    
    heights[r][c] = height above sea level of the cell at (r, c).

    The island receives a lot of rain, and 
    the rain water can flow to neighboring cells directly 
        north, 
        south, 
        east, and 
        west 
        
    if the neighboring cell's height <= to the current cell's height. 
    Water can flow from any cell adjacent to an ocean into the ocean 
        (so I guess we let ocean height = -inf?)

    Return a 2D list of grid coordinates result, 
        where result[i] = [ri, ci] denotes that rain water can flow 
        from cell (ri, ci) to both the Pacific and Atlantic oceans.

    Exaple 1:
        Input: heights = [
    P       0000000000000
            0[1,2,2,3,5]0
            0[3,2,3,4,4]0
            0[2,4,5,3,1]0
            0[6,7,1,4,5]0
            0[5,1,1,2,4]0
        ]   0000000000000  A
    
    Output: [
        [0,4], --> corner
        [1,3], 
        [1,4],
        [2,2],
        [3,0],
        [3,1],
        [4,0]
    ]

    Intuition:
        island = immutable, directed graph
            each cell = a vertex
            each of 4 directions - edges
            heights >= 0

        goal: 
            find all vertices with a path to both:
                P = { row = -1 , or col = -1} AND
                A = { row = m + 1, or col = n + 1}

    EC:
        - empty grid ==> []
        - all heights < 0 --> ValueError

    Approach:
        let e = m * n

        1. Brute Force:
            DFS on each cell --> see if path to both oceans
            O(e^2)

        2. Idea #2: ---> does not cover all possible inputs
            for each row:
                find tallest
                    DFS only on tallest
                    see if it can reach both - if so, add to set

        3. Idea #3 --> find the points in set A AND P
            1
    """
    def pacific_to_atlantic(self, island: List[List[int]]) -> List[List[int, int]]:
        ### HELPERS
        def _get_neighbors(row, col):
            return [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]

        def _is_in_both(ri, ci):
            """plan: iterative DFS w/ visited set"""
            is_in_p, is_in_a = False, False
            stack, visited = list([(ri, ci)]), set()

            while stack:
                row, col = stack.pop()
                # check oceans
                if row == 0 or col == 0:
                    is_in_p = True
                if row == len(island) - 1 or col == len(island[0]) - 1:
                    is_in_a = True
                visited.add((row, col))
                # add neighbors
                for nr, nc in _get_neighbors(row, col):
                    if -1 < nr < len(island) and -1 < nc < len(island[0]):
                        if (nr, nc) not in visited:
                            if island[nr][nc] <= island[row][col]:
                                stack.append((nr, nc))

            return is_in_p and is_in_a

        ### GUARD
        if not island or not island[0]:
            return []

        ### DRIVER
        coords = list()

        for ri in range(len(island)):  # row index
            for ci in range(len(island[0])):  # col index

                if _is_in_both(ri, ci) is True:
                    coords.append([ri, ci])
        
        return coords
