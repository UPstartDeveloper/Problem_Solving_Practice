import math

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        Input:
            dims of mul table
            k ----> which value to index (1-index)
        Output:
            k smallest produ f====> sorted(products)
            
        ASSUME fits in memory
            
        Intuition:
            - heaps
            - dynammic programming
            
        EC:
            1) invalid inputs - negatives, k is too large ---> ValueError
            2) TODO
            
        Approach:
        
            1) Brute force ---> sorting
                A: make the table --- 2D -- products ---> O(m*n)
                B: sort all the eement ----> 1D array  ---> linearithmic
                3) return prod[k-1] elements  ---> O(1)
                
            2) Searching
                A: make the table --- 2D -- products ---> O(m*n)
                B: search for kth ----> 
                    k = 6
                    m = 2
                    n = 3
                    row_solution = k / n ---> 2nd row
                    col_solution = k - (k / n) - 1
                    
                    k - (k / n) - 1
                    6 - ((6/ 2)) - 1 =
                    6 - 3 - 1 = 2
                    
            3) TODO
            
        m = 2
        n = 3
        
        [0, 0, 0]
        [0, 0, 0]
                    
        """
        ### HELPERS
        def _compute_mul_table_2d(m, n):
            # A: init the table
            table = list()
            # B: populate the table w/ each row
            for row_factor in range(1, m + 1):
                row = list()
                for col_factor in range(1, n + 1):
                    row.append(row_factor * col_factor)
                table.append(row)
            # C: all done!
            return table
        
        def _compute_mul_table_1d(m, n):
            # A: init the table
            table = list()
            # B: populate the table w/ each row
            for row_factor in range(1, m + 1):
                for col_factor in range(1, n + 1):
                    table.append(row_factor * col_factor)
            # C: all done!
            return table
        
        def _search_for_answer(k, table):
            """TODO[test]"""
            num_rows, num_cols = len(table), len(table[0])
            row_solution = math.ceil(k / num_cols) - 1
            # col_solution = # TODO
            return table[row_solution][col_solution]
        
        ### DRIVER
        # A: make the table --- 2D -- products ---> O(m*n)
        # table = _compute_mul_table_2d(m, n)  
        table = _compute_mul_table_1d(m, n)  
        # B: search for kth
        return sorted(table)[k - 1]
    
"""
m = 2, n = 3, k = 6 ---> k = 5


t = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

rf = 1, 2
cf = 1,2, 3 -- 1, 2 ,3

r = [1, 2, 3]

=-==========
t = [[1, 2, 3], [2, 4, 6], [3, 6, 9]], k = 6, 5

num_rows = 2, num_cols = 3

k / 3 ---> 2

k - 3 - 1 --> 2

rs = 1


col_solution----> k - num_elems_already_traversed

"""
