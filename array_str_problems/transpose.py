from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Clarifications:
            1. Input:
                - non-empty
                - rectangular
            
            2. ASSUMEs
                - ok to do this out of place
                - input is not always a square --> dims can chage
                - np not allowed
                - input has 2D only 
                
        Intuition:
            - output is where every row of input is now a col
            - shape of output is reverse of input shape
            
        Edge Cases:
            - all values are the same? --> return input right away
        
        
        [    v
            [1,2,3],---------> [1, 4, 3]        [1, 4, d]
                                   v
            [4,5,6]            [2, 5, 6]  --->  [2, 5, d]
                                                       v
                               [d  d   d]       [3, 6  d]
            
        ]
        2 x 3 -----------> 3 x 2
        
        Approach:
        
        1) Out of Place:
            - new array
            - iterate over each col of input
                - add it as a row to the output
            - return the output
            
        2) Inplace:
            - add rows or cols of "d" to make the matrix a square
            - traverse the main diagonal
                - switch values (iterate along r, d vectors)
            - at the end, delete all the "d" chars
        
        """
        ######## IN-PLACE ################
        def squarify(matrix):
            def add_rows(matrix, r):
                for _ in range(r):
                    matrix.append(["d" for _ in range(num_cols)])
            
            def add_cols(matrix, c):
                for row_index in range(num_rows):
                    matrix[row_index].extend(["d" for _ in range(c)])
            
            # decide to add rows or cols
            num_rows, num_cols = len(matrix), len(matrix[0])
            
            if num_rows > num_cols:
                add_cols(matrix, num_rows - num_cols)
            
            elif num_rows < num_cols:
                add_rows(matrix, num_cols - num_rows)
        
        def transpose(matrix):
            # init indicies
            row_ndx, col_ndx = 0, 0
            # traverse the main diagonal
            num_rows, num_cols = len(matrix), len(matrix[0])
            while row_ndx < num_rows and col_ndx < num_cols:
                # iterate along the right and down dirs
                right_vector = [row_ndx, col_ndx + 1]
                down_vector = [row_ndx + 1, col_ndx]
                while right_vector[1] < num_cols and down_vector[0] < num_rows:
                    # swtich values in-place
                    right_val, down_val = (
                        matrix[right_vector[0]][right_vector[1]],
                        matrix[down_vector[0]][down_vector[1]]
                    )
                    matrix[right_vector[0]][right_vector[1]] = down_val
                    matrix[down_vector[0]][down_vector[1]] = right_val
                    # keep moving in the right and down directions
                    right_vector[1] =  right_vector[1] + 1
                    down_vector[0] = down_vector[0] + 1
                # move to the next elem in the diagonal
                row_ndx += 1
                col_ndx += 1
        
        def clean(matrix):
            '''remove any "d" chars in the matrix
               TODO: optimize for time and space
            '''
            for row_index in range(len(matrix)):
                matrix[row_index] = [val for val in matrix[row_index] if val != "d"]
            # remove empty rows
            for row_index in range(len(matrix) - 1, -1, -1):
                if len(matrix[row_index]) == 0:
                    matrix.pop(row_index)
    
    
        # - add rows or cols of "d" to make the matrix a square
        squarify(matrix)
        # - traverse the main diagonal
        transpose(matrix)
        # remove any added chars
        clean(matrix)
        return matrix
        