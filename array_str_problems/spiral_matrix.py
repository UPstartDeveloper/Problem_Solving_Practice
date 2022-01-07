from typing import List

class Solution:
    def __init__(self):
        self.dirs = {
            "right": (0, 1),
            "down": (1, 0),
            "up": (-1, 0),
            "left": (0, -1)
        }
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Leetcode: https://leetcode.com/problems/spiral-matrix/
        
        Input/Problem:
            - rect matrix
            - immutable
            - int
            - ASSUME not empty
            
        Output:
            - return ordring of elems in "spiral"
            - right, down, left, up (always)
            
        Intuition:
            array traversal
            vectors
            
        EC: 
            - invalid input (wrong dtype, empty, too large)
            
        Approach:
            
            1) DIY:
                A: define motion vectors (R, D, L, U)
                B: define horizontal and vertical boundaries
                C: init output = []
                D: begin traversal --> init dir is R, coords = 0,0
                    a: add elem at current coords to output
                    b: if at edge ---> change current_dir
                    c: always --> move another step in current_dir
                E: return output
                
                When to Bring the Limits Further "Inside":
                    Hor --> when dir changes to "Right"
                    Ver --> when dir changes to "Up"
                    
                Setting Limits
                horizontally
                    - limits defined by num of cols in mat
                    - init it to len(mat[0]) - 1 - hor_limit, right
                    - goes left: hor_limit
                    - goes right: 
                        hor_limit += 1
                        len(mat[0]) - 1 - hor_limit
                        
                vertically
                    - limits defined by num of rows in mat
                    - init it to len(mat) - 1 - ver_limit, down
                    - goes up: 
                        ver_limit += 1
                        ver_limit
                    - goes down: 
                        len(mat) - 1 - ver_limit
                
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
        output = list()
        current_dir = "right"
        coords = (0, 0)
        hor_limit, ver_limit = 0, 0
        # B: begin traversal 
        NUM_ELEMS = len(matrix) * len(matrix[0])
        while len(output) < NUM_ELEMS:
            # a: add elem at current coords to output
            output.append(matrix[coords[0]][coords[1]])
            # b: if at edge ---> change current_dir
            if _is_at_edge(current_dir, coords, hor_limit, ver_limit):
                current_dir = _change_dir(current_dir)
                hor_limit, ver_limit = (
                    _change_limits(current_dir, hor_limit, ver_limit) 
                )
            # c: always --> move another step in current_dir
            coords = _get_next_coords(coords, current_dir)
        # C: all done!
        return output
