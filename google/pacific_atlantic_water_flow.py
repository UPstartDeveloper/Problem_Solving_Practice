from typing import List


class Solution:
    """
    LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/
    Credit to gabhinav001 for solution: https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/2161314/simple-dfs-beats-98

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
    def pacific_atlantic(self, board: List[List[int]]) -> List[List[int]]:
        ### HELPERS
        def _get_neighbors(row, col):
            return [
                (row + 1, col),  # down
                (row - 1, col),  # up
                (row, col + 1),  # right
                (row, col - 1),  # left
            ]

        def reachable(stack):
            """iterative DFS on a directed graph, w/ potential cycles"""
            visited = set()
            
            while stack:
                # visit operation
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    row, col = node 

                    # visit all neighbors
                    for neighbor_row, neighbor_col in _get_neighbors(row, col):
                        nr, nc = neighbor_row, neighbor_col
                        # validation checks
                        if -1 < nr < len(board) and -1 < nc < len(board[nr]):
                            if (nr, nc) not in visited:
                                if board[row][col] <= board[nr][nc]:
                                    stack.append((nr, nc))
            # all done!
            return visited
        
        ### DRIVER
        # 1: find the set of all coords that can reach Pacific
        stack = list()
        # push first row
        for j in range(len(board[0])):
            stack.append((0, j))
        # push first col
        for i in range(len(board)):
            stack.append((i, 0))

        can_reach_pacific = reachable(stack)
        
        # 2: find the set of all coords to reach Atlantic
        stack.clear()
        # last row
        for j in range(len(board[0])):
            stack.append((len(board)-1, j))
        # last col
        for i in range(len(board)):
            stack.append((i, len(board[0])-1))
    
        can_reach_atlantic = reachable(stack)
        
        # 3: find the "overlap"
        return can_reach_pacific and can_reach_atlantic        
