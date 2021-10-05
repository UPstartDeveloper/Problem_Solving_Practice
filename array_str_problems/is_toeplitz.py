def is_Toeplitz(arr):
    # ----- Helper -----
    def check_diagonal(start):
        # copy the first element
        row_index, col_index = start
        first = arr[row_index][col_index]
        # move down and to the right, as long as we're still in the matrix
        row_index += 1
        col_index += 1
        while row_index < len(arr) and col_index < len(arr[0]):
            # check each succsssive elemem == first elem
            next_elem = arr[row_index][col_index]
            if next_elem == first:
                row_index += 1
                col_index += 1
            # if not - --> F
            else:
                return False
        # if we exit the matrix --> T
        return True

    # ------ rest of the function -------

    if len(arr) > 0:  # [[]]
        # A: iterate over the first row
        if len(arr[0]) > 0:
            for col_index, element in enumerate(arr[0]):  # n iteration (# cols)
                if check_diagonal((0, col_index)) is False:
                    return False
        # B: repeat over the first col
        if len(arr) > 1:
            for row_index, row in enumerate(arr[1:]):
                if check_diagonal((row_index, 0)) is False:
                    return False
    return True


"""
[
  [1, 2]
  [3, 1]
]

col   elem                  row     col   fi
0     1                       0     0     1
                              1     1
                              2     2
	@param arr: int[][]
	@return: bool
  
  [[1,2,3,4],
   [5,1,2,3],
   [6,5,1,2]]
   
  - The matrix can be any dimensions
  - empty rows, empty cols
  
  Idea:
  
  row_idex +1 col_index +1
  
  Intuition: first row and first col --> start of each diagonal
  
  Approach: iterate down each diagonal
            check it, 
            return True if they all meet the conditions
            
  Edge cases: empty matrix [[]]
              empty rows (but all the rows are empty)            
	"""
