from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Input:
        [[0,0,0],
         [0,1,0],
         [0,0,0]]

        Output:
        [[0,0,0],
         [0,1,0],
         [0,0,0]]
         
        Clarifying Q's:
        so if an element is 0, it's distance is zero? yes
        so each elem in the output corresponds to the same pair of indices in the input? yes
        so I take it the input is immutable? yes
        am I allowed to use the deque class?
        
        Assume:
        that the matrix is always nxn (square)
        cannot go diagonal
        
        Intuition:
        
        use BFS to find the shortest distance from one element in the matrix to a 0
        do it for all the elements
        collect them in corresponding order of indicies in an output matrix (return)
        
        Approach:
        
        helper function for finding_nearest_zero
        
        driver function - iterate over the matrix cells
        
        Edg 
        
        
        
        """
        # Helper -------------------------------------------------------------
        def find_nearest_zero(row_index, col_index):
            # A: define the directions we can go in 
            DIRECTIONS = [
                (0, 1),  # right
                (0, -1),  # left
                (1, 0),  # down
                (-1, 0),  # up
            ]
            # B: init a queue, and a set of visited nodes
            q, visited = deque(), set()
            # D: BFS
            q.append((row_index, col_index, 0))
            while len(q) > 0:
                # dequeue the next item from the queue (row, col, distance_so_far)
                row_index, col_index, distance = q.popleft()
                # visit the element at this cell in the input matrix
                cell = matrix[row_index][col_index]
                visited.add((row_index, col_index))
                # if it's a zero - return the distance so far
                if cell == 0:
                    return distance
                # otherwise enqueue all the neighboring rows, cols, and distance + 1
                for delta_row, delta_col in DIRECTIONS:
                    neighbor_row, neighbor_col = row_index + delta_row, col_index + delta_col
                    if 0 <= neighbor_row < len(matrix) and 0 <= neighbor_col < len(matrix[0]):
                        if (neighbor_row, neighbor_col) not in visited:
                            q.append((neighbor_row, neighbor_col, distance + 1))
        
        # Driver -------------------------------------------------------------
        # A: init the output matrix
        output = list()
        # B: iterate over each row in the input
        for row_index, row in enumerate(matrix):
            # C: init a new row to go in the output
            out_row = list()
            # D: iterate over the col elems in this row
            for col_index, cell in enumerate(row):
                # E: BFS from our current cell
                distance = find_nearest_zero(row_index, col_index)
                # F: add the distance to the output row
                out_row.append(distance)
            # G: add the row to the output
            output.append(out_row)
        # H: return the output matrix
        return output
        
        
"""
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]













Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
"""
     