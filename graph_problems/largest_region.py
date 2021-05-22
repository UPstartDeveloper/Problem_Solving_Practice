#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys

# Another application of BFS on a graph.
# Source: https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    """
    Clarifications:
    - return the size of the largest "region" of connected vertices
    - ASSUME graph is mutable - helps to not "double" count a region of 
        land
    - the matrix CAN be empty, or is a rectangle
    - vertices CAN connect diagonally, as well as horizontally/vertically
    - only 0s or 1s
    - ASSUME deques are allowed
    
    110 ---> 000 --> 000 --> [3, 1] ---> 3
    100      000     000
    001      001     000
        
    Intuition:
        filled cell = vertex of directed graph
        BFS each connect comp of filled cells
        
    Approach:
        A: define the edge vectors (going from one node to another)
        B: init count for size_largest_region = 0
        C: traverse the MATRIX
            1: if filled cell found, start BFS w/ a queue 
            2: dequeue each node, 
            3: mark the cell 0, enqueue neighbors
            4: after BFS, update largest_size if needed
        D: return size_largest_region
    
    Edge Cases
        empty graph ---> assume we return 0
        no 1s --> return 0
        all 1s --> return n * m
    """
    # A: define the edge vectors (going from one node to another)
    EDGES = [
        # up
        (-1, 0),
        # down
        (1, 0),
        # left
        (0, -1),
        # right
        (0, 1),
        # upper right
        (-1, 1),
        # lower left
        (1, -1),
        # lower right
        (1, 1),
        # upper left
        (-1, -1)
    ]
    # B: init count for size_largest_region = 0
    size_largest_region = 0
    # C: traverse the MATRIX
    for row_ndx in range(len(matrix)):
        for col_ndx in range(len(matrix[0])):
            if matrix[row_ndx][col_ndx] == 1:
                # 1: if filled cell found, start BFS w/ a queue 
                q = deque([(row_ndx, col_ndx)])
                size_current = 0
                while len(q) > 0:
                    # 2: dequeue each node
                    cell_row, cell_col = q.popleft() 
                    # 3: mark the cell 0, enqueue neighbors
                    if matrix[cell_row][cell_col] == 1:
                        matrix[cell_row][cell_col] = 0
                        size_current += 1
                        for row_diff, col_diff in EDGES:
                            row_neighbor = cell_row + row_diff
                            col_neighbor = cell_col + col_diff
                            if 0 <= row_neighbor < len(matrix):
                                if 0 <= col_neighbor < len(matrix[0]):
                                    neighbor = matrix[row_neighbor]
                                    neighbor = neighbor[col_neighbor]
                                    if neighbor == 1:
                                        # prevent double-counting
                                        coords = (
                                            row_neighbor, col_neighbor)
                                        q.append(coords)
                # 4: after BFS, update largest_size if needed
                if size_current > size_largest_region:
                    size_largest_region = size_current
                    size_current = 0
    # D: return size_largest_region
    return size_largest_region
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
