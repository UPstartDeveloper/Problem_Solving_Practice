#!/usr/bin/env python3

"""
Cracking the Coding Interview 8.2:

Robot in a Grid: Imagine a robot 
sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, 
but certain cells are "off limits" such that the robot cannot step on them. 

Design an algorithm to find a path for the robot 
from the top left to the bottom right.

Assumptions:
- there is guaranteed to be at least one row in the grid
- there is guaranteed to be a path from the upper left to 
    bottom right corners

Time: O(V)
Space: O(V)

What I learned: keep in mind the return value for EVERY stack frame
that hasn't been popped yet! The function doesn't really exit until
all the stack frames do.

"""


def find_path(grid, stack=None, path=None):
    '''Finds a path from the start till the end, using DFS.'''
    # Base Case: for the first call, init the stack and path
    if stack is None and path is None:
        stack, path = list(), list()
        # push the starting cell onto the stack
        stack.append((0, 0))
        return find_path(grid, stack, path)
    # Recursive Case: check what's in the next cell
    # print(f"Stack: {stack}")
    next_cell = stack.pop()
    # visit the next cell - add it to our path so far
    path.append(next_cell)
    # check if we have reached the destination
    row, col = next_cell
    # print("row and col", row, col)
    if (row == len(grid) - 1) and (col == len(grid[0]) - 1):
        print(f"Path found: {path}")
        return path
    # otherwise, see if we can continue going down
    neighbors = [
        (row + 1, col), (row, col + 1)
    ]
    for neighbor in neighbors:
        n_row, n_col = neighbor
        if n_row < len(grid) and n_col < len(grid[0]) and grid[n_row][n_col] != 0:
            stack.append(neighbor)
            path = find_path(grid, stack, path)
            # stop early, if dest. found
            if path[-1] == (len(grid) - 1, len(grid[0]) - 1):
                break
    # when we hit a dead end, that's not the destination
    else: # remove cell on the dead end path
        path.pop()
    return path


if __name__ == "__main__":
    # init a test grid - 0 means "the robot can't go here"
    grid = [
        [1, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1]
    ]
    # test if the output from the function is correct
    print(find_path(grid))
    """
    path = [
        (0, 0),
        (0, 1),

    ]

    stack = [(0, 1), (0, 2)]
    """
