class Solution:
    
    def __init__(self):
        self.paths_count = 0
    
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Leetcode: https://leetcode.com/problems/unique-paths/
        
        Input/Problem:
            - dims of a rectangular grid
            - path-finding to get the TL ---> BR
        
        Output:
            - number of paths
            
        Intuition
            - backtracking ---> find all unique paths
        
        EC: 
            1) m and n == 1 ----> 1
            2) m or n <= 0 -----> ValueError
            3) TODO
            
        Approach:
            
            1) Brute Force ==> Backtracking
                A: create a grid - m*n
                B: find all unique paths --> set ----> ((x1, y1), (x2, y2)) - exponential
                C: return len(paths_set)
                
            2) Tree ---> backtracking
            
            m = 3, n = 2
            
            |   S    |       |
            |        |       |
            |        |   F   |
            
            base case 1: outside the grid---> return
            base case 2: at the finish ---> count_paths += 1
            recursive case: in the grid ---> go to the D/R neighboring cells
            
                      [cooords = 0, 0 ]]
                        D   /     \   R
                           /       \
              [cooords = 1, 0 ]]   [cooords = 0, 1 ]]
              D   /     \   R
                 /       \
    [cooords = 2, 0 ]] 
     D   /      \   R
        /        \
[cooords = 3,0]]  [cooords = 2, 1 ]] 
     
                                
        TEST: m = 3, n = 2
        """
        ### HELPERS
        def _count_paths_bt(coords) -> int:
            row, col = coords
            # base case 1: outside the grid---> return
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            # base case 2: at the finish ---> count_paths += 1
            elif row == (m - 1) and col == (n - 1):
                self.paths_count += 1
            # recursive case: in the grid ---> go to the D/R neighboring cells
            else:
                _count_paths((row + 1, col))  # down
                _count_paths((row, col + 1))  # right
            return self.paths_count
        
        def _count_paths_dp():
            # A: init dp table
            table = [
                [0 for _ in range(n)]
                for _ in range(m)
            ]
            # B: handle edge cases - last col and row
            for row_index in range(m):
                table[row_index][-1] = 1
            for col_index in range(n):
                table[-1][col_index] = 1
            # C: solve recursive cases
            for row_index in range(m-2, -1, -1):
                for col_index in range(n-2, -1, -1):
                    # use the down and right neighbors to solve
                    table[row_index][col_index] = (
                        table[row_index + 1][col_index] +
                        table[row_index][col_index + 1]
                    )
            # D: return the answer
            return table[0][0]
        
        ### DRIVER
        # A: handle EC
        if m == 1 or n == 1:
            return 1
        elif m < 1 or n < 1:
            raise ValueError("Invalid grid dims")
        # B: handle rest of cases
        # return _count_paths_bt((0, 0))  # Backtracking 
        return _count_paths_dp()  # Dynamic Programming
