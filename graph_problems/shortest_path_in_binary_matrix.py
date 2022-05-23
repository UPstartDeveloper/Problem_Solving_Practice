from collections import deque


class Solution:

    DIRECTIONS = [
        # cardinal dirs
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        # diagonals
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Intuition:
            BFS ---> shortest path
            
        Input:
            binary sq matrix
            assumption that it's mutable
            
        Output:
            min(dist(clear_path))
                clear_path - all 0's + 8-directions
                
        Approach:
            
            1) iterative BFS:
            
                queue --> node, dist_so_far
                
                pop queue --> check if bottom right
                    return dist_so_far
                    
                if nothing --> -1
                
        EC:
            
            - ValueError --> non-binary, no grid, no grid columns
            - if TL corner or BR != 0 --> -1
        
        [
            [1,0,0],
            [1,1,0],
            [1,1,0]
        ]
        """
        ### HELPERS
        def _bfs(grid):

            queue = q = deque([(0, 0, 1)])  # coords + dist_so_far

            while q:

                # dequeue
                row, col, dist_so_far = q.popleft()

                # "visit" operation
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return dist_so_far

                else:  # avoid revisit
                    grid[row][col] = -1

                # enqueue the neighbors
                for delta_row, delta_col in self.DIRECTIONS:
                    neighbor_r, neighbor_c = (row + delta_row, col + delta_col)
                    if -1 < neighbor_r < len(grid) and -1 < neighbor_c < len(grid[0]):
                        if grid[neighbor_r][neighbor_c] == 0:
                            q.append((neighbor_r, neighbor_c, dist_so_far + 1))

            return -1

        ### DRIVER
        # A: check ECs - TODO[check-non-binary, jagged matrix]
        if len(grid) == 0 or not grid[0]:
            raise ValueError("empty or jagged matrix")

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        # B: find the distance (via BFS)
        min_dist = _bfs(grid)

        # C: return the distance
        return min_dist  # -1 or pos int


"""
0111
0110
0011
1000


"""
