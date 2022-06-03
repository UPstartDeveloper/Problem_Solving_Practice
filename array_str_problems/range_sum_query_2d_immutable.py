from typing import List


class NumMatrix:
    """
    LeetCode: https://leetcode.com/problems/range-sum-query-2d-immutable/
    
    input:
        matrix: int[][] - int, immutable, pos/neg, non-empty, dupes, unsorted
                          non-jagged
        
        queries - defines a rectangle, (guaranteed to be valid indices)
        we output the sum
        
    Intuition:
        array slicing 
        iterations
        memoization
        
    EC: 
        rectangle of 1 --> return 1 value
        
    Approach:
    
        1) Human Approach:
    """
    def cum_sum(self, arr):
        summed = list([0])
        runninng_sum = rs = 0
        for num in arr:
            rs += num
            summed.append(rs)
        return summed
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dp_table = [self.cum_sum(row) for row in matrix]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        
        for row_index in range(row1, row2 + 1):
            row_total = (
                self.dp_table[row_index][col2 + 1] -
                self.dp_table[row_index][col1]
            )
            total += row_total
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
