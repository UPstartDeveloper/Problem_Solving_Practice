from typing import List

class Solution:
    def __init__(self):
        self.dirs = {
            "right": (0, 1),
            "down": (1, 0),
            "up": (-1, 0),
            "left": (0, -1)
        }
        
    def generate_matrix(self, n: int) -> List[List[int]]:
        """
        Leetcode: https://leetcode.com/problems/spiral-matrix-ii/
        
        similar to another problem
            given a rectangular matrix
                traverse it in a sprial
            return the elements in the order they appear
            
        
        diff
            given a side length of a sq. matrix
                make + populate the matrix
            return the matrix
            
        Dir Changes:
        # F: onChange:update direction, hor/ver trans
            R -> D
            D -> L ---> decrement the vertical_translation
            L -> U 
            U -> R ---> decrement the horizontal_translation
        
        """
        ### HELPERS
        def _get_next_coords(current_coords, current_dir):
            change_in_coords = self.dirs[current_dir]
            return (
                current_coords[0] + change_in_coords[0],
                current_coords[1] + change_in_coords[1]
            )
        
        def _is_at_edge(current_dir, coords, hor_limit, ver_limit):
            if current_dir == 'right':
                return coords[1] == len(matrix[0]) - 1 - hor_limit
            elif current_dir == 'left':
                return coords[1] == hor_limit
            elif current_dir == 'up':
                return coords[0] == ver_limit
            elif current_dir == 'down':
                return coords[0] == len(matrix) - 1 - ver_limit
            
        def _change_dir(current_dir):
            if current_dir == "right":
                return "down"
            elif current_dir == "down":
                return "left"
            elif current_dir == "left":
                return "up"
            else:  # current_dir == "up"
                return "right"
            
        def _change_limits(current_dir, hor_limit, ver_limit):
            if current_dir == "right":
                hor_limit += 1
            elif current_dir == "up":
                ver_limit += 1
            return hor_limit, ver_limit
        
        ### MAIN
        # A: init values
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        current_dir = "right"
        coords = (0, 0)
        hor_limit, ver_limit = 0, 0
        count = 1
        # B: begin traversal 
        while count <= n * n:
            # a: add elem at current coords to output
            matrix[coords[0]][coords[1]] = count 
            count += 1
            # b: if at edge ---> change current_dir
            if _is_at_edge(current_dir, coords, hor_limit, ver_limit):
                current_dir = _change_dir(current_dir)
                hor_limit, ver_limit = (
                    _change_limits(current_dir, hor_limit, ver_limit) 
                )
            # c: always --> move another step in current_dir
            coords = _get_next_coords(coords, current_dir)
        # C: all done!
        return matrix
        
        
