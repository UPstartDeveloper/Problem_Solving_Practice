"""
Eight Queens: 

Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board 
so that none of them share the same 
row, 
column, or 
diagonal. 

In this case, "diagonal" means all diagonals, not just the two that bisect the board.

Test Input: n = 8

Output: none
StdOut:

"
    0   1   2   3   4   5   6   7
0   Q   X   X   X   X   X   X   X
1   X   X   X   Q   X   X   X   X
2   X   Q   X   X   X   X   X   X
3   X   X   X   X   Q   X   X   X
4   X   X   Q   X   X   X   X   X
5   X   X   X   X   X   Q   X   X
6   X   X   X   X   X   X   X   X
7   X   X   X   X   X   X   X   X

queens = 6, 5, 4, 3, 2

Clarifying Questions:
- how should the output look like? is the above ok?
    - numered rows and columns?
    - X marks where the queens are?
    - do we need to mark every cell that isn't filled by a queen/off-limits
    - and each board should start on a new line?
- no inputs?
- do all 8 queens needs to be on the board for it to count as a permutation?

Brainstorm:

1) DIY
queens = 8

choices --> the board
constraint --> the rules above, queens = 0 for it to be a solution
goal -->  get all the unique placements


- need to make sure that we follow the rules (maybe mark off the rows, cols, and diagonals?)
- need a way to make sure the arrangements that are printed are unique

Approach:
Base Case: queens == 0:
    return out the arrangement
    reset the board
    reset queens = 8
    call the function again
Recursive Case: queens > 0:
    - iterate over the rows and columns
        - place a Q on the first spot that's not X or B
        - check off the rows, columns, and diagonals
        - decrement queens
    - at end of the for loops
        - if the number of queens != 0 --> STOP
        - if it is, call the base case (print the board)

Helper Functions:
- check_off_row
    - same row, col ++
- check_off_col
    - row ++, same col
- check_off_diagonals
    - row ++, col ++
    - row --, col --
- reset_board:
    - remove the X's
    - replace the Q's w/ B's - "used before"

- how do we know when to stop?
    - guess it there should be enough 
"
"""