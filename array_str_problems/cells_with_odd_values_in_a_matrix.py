from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        ### HELPERS
        def increment(index, matrix, mode):
            if mode == 'row' and index < m:
                for col_index in range(n):
                    matrix[index][col_index] += 1
            elif mode == 'col' and index < n:
                for row_index in range(m):
                    matrix[row_index][index] += 1
                    
        def _count_odds(matrix):
            count = 0
            for row in matrix:
                for val in row:
                    if val % 2 > 0:
                        count += 1
            return count
        
        ### DRIVER code:
        # A: init the matrix
        matrix =[
            [0 for _ in range(n)]
            for _ in range(m)
        ]
        
        # B: traverse the indicies
        for row, col in indices:
            # apply the transformation
            increment(row, matrix, mode='row')
            increment(col, matrix, mode='col')
            
        # C: return final matrix
        return _count_odds(matrix)
