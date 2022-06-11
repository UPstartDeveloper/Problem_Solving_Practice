from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        LeetCode: https://leetcode.com/problems/max-area-of-island/
        Input:
            grid:
                2D array
                bits
                assume - it's mutable
                1 - land
                0 - water
                
        Output:
            max(areas)
            
        Intuition:
            DFS/BFS
            
        EC:
            empty grid? --> 0
            jagged grid? --> should be able to support, so we're fine
            non-bit - ValueError
        
        Approach:
        
            1) mutative, iterative DFS
            
                init a set of areas
                traverse the grid
                    DFS each island (each 1 is a node, has <= 4 edges, undirected)
                    add its area
                    
                return max area
        Time: O(e), where e = # of elements in matrix
        Space: O(e), in the worst case when grid is all 1's
        """
        
        ### HELPERS
        def _get_neighbors(ri, ci):
            return [
                (ri, ci + 1),
                (ri, ci - 1),
                (ri + 1, ci),
                (ri - 1, ci)
            ]
        
        def _dfs(ri, ci):
            '''iterative DFS (top of stack is last index)'''
            size = 0
            stack = list([(ri, ci)])
            
            while stack:
                ri, ci = stack.pop()
                if grid[ri][ci] == 1:
                    size += 1
                    grid[ri][ci] = 0  # no double dipping
                    # search neighbors
                    for nr, nc in _get_neighbors(ri, ci):
                        if -1 < nr < len(grid) and -1 < nc < len(grid[nr]):
                            stack.append((nr, nc))
            
            return size
        
        ### DRIVER
        # init largest area seen so far
        max_area = 0
        
        # find all areas
        for ri in range(len(grid)):
            row = grid[ri]
            for ci in range(len(row)):
                elem = grid[ri][ci]
                # edge case for invalid grid values
                if not (elem == 0 or elem == 1):
                    raise ValueError(f"Expected bit at {ri, ci} in grid, \
                                      instead found a {type(elem)}.")
                # area of ONE island
                elif elem == 1:
                    size = _dfs(ri, ci)
                    max_area = max(max_area, size)
        # all done!    
        return max_area
