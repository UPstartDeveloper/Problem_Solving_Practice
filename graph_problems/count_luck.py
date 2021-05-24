#!/bin/python3

import math
import os
import random
import re
import sys

# Problem Source: https://www.hackerrank.com/challenges/count-luck/problem
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def countLuck(matrix, k):
    """
    CLARIFICATIONS: 
    
    - k = Ron's guess
    - non-empty matrix = str []
    - 1 M = starting point
    - 1 * = goal
    - X = no pass
    - GUARANTEED 1 path
    - move LEFT, RIGHT, UP, and DOWN
    - matrix mutable - ASSUME not
    
    Intuition:
    need to count number of times we backtrack (hit a fork),
    then compare it to k once we reach the goal
    
    Approach:
    
    1) iterative DFS, use space to avoid mutation
    
        A: init waves = 0
        B: locate the M
        C: DFS from M (dfs_helper) - init a stack w/ M
            1) iterate until we hit the *, then break
                2) push all .'s from our spot
                3) if we push more than 1 . at a time, increment waves   
            # 1) Base Case: 1 .
            #     - move to that .
            # 2) Recursive Case: 
            #     - increment waves
            #     - push . onto the stack, if found in DIRS
        D: compare waves w/ k
    
    Edge Cases:
    - empty matrix - not possible
    - multiple paths - not possible     
    """
    def find_start():
        '''TODO: return row and col of "M"'''
        # save the coords of the M
        row_index = 0
        # traverse rows
        while row_index < len(matrix):
            row = matrix[row_index] 
            col_index = 0
            # traverse cols
            while col_index < len(row):
                # check each char
                char = row[col_index]
                # M found
                if char == "M":
                    return (row_index, col_index)
                # if not found, move on to the next char
                col_index += 1
            # move on to the next row
            row_index += 1
        # M not found
        return (-1, -1)
    
    def is_guess_correct(waves: int) -> str:
        '''TODO: return whether RON was correct'''
        guess = k
        # correct
        if waves == guess:
            return "Impressed"
        # incorrect
        return "Oops!"
    
    # A: init waves = 0 and directions
    waves = 0
    DIRECTIONS = [
        # up
        (-1, 0),
        # down
        (1, 0),
        # left
        (0, -1),
        # right
        (0, 1)
    ]
    # B: locate the M
    start = find_start()
    # C: DFS from M (dfs_helper) - init a stack w/ M
    stack = [start]
    visited = set()
    # 1) iterate until we hit the *, then break
    while len(stack) > 0:
        spot_row, spot_col = stack.pop()
        visited.add((spot_row, spot_col))
        current_char = matrix[spot_row][spot_col]
        # end the search
        if current_char == "*":
            break
        # continue the search
        else:
            added = 0
            # 2) push all valid .'s from our spot
            for row_diff, col_diff in DIRECTIONS:
                neighbor_row = spot_row + row_diff
                neighbor_col = spot_col + col_diff
                if 0 <= neighbor_row < len(matrix):
                    if 0 <= neighbor_col < len(matrix[neighbor_row]):
                        neighbor_coords = (neighbor_row, neighbor_col)
                        if not neighbor_coords in visited:
                            neighbor = matrix[neighbor_row][neighbor_col]
                            if neighbor == "." or neighbor == "*":
                                stack.append(neighbor_coords)
                                added += 1
            # 3) if we push more than 1 . at a time, increment waves
            if added > 1:
                waves += 1  
    # D: compare waves w/ k
    return is_guess_correct(waves)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
