"""
CtCI 7.6

Jigsaw: 
Implement an NxN jigsaw puzzle. 

Design the data structures and explain an algorithm to solve the puzzle. 
You can assume that you have a fitsWith method which, 
    when passed two puzzle edges, 
    returns true if the two edges belong together.

1) Scope:
    a) who - 1-player
    b) what - 
        1) series of nxn pieces, 
            each belongs somewhere in the grid
            only way of knowing is by clues, given by:
                - shape of piece (e.g. "straight edges")
                - other pieces it "fitsWith()" - logic, 
                - appearance of piece - ASSUME it can be left out 
                    (try to localize where it'd be on the board,
                    based on the place it is on the actual image)
    c) why - the goal:
        - find a place for each piece
    d) how
        - place pieces 1 by 1 
        - start at the edges, work around the boundary, and move it
            - DFS/backtracking

2) Core Objects:
    1) Grid:
        - array of Pieces
            - --> count of unfinished pieces
        - matrix of n x n spaces - initially null
            - space poplulated --> pter to a Piece
            - each Piece --> <= 8 neighbors
        - place(Piece)
            - A: mutate the matrix and the list
            - B: return the coords where the piece is now in the gird
    2) Piece - aka "vertex"
        - is_corner: boolean
        - is_horizontal: boolean
        - dict {4 x self.PuzzleEdge: --> PuzzleEdge}
    3) PuzzleEdge:
        - piece
        - side: 'right', 'left'
        - fits_with()

3) Relationships: Grid ----> Piece --> PuzzleEdge

[P1 P2 N N N N N N N N N N N N N N N ]
[N N N N N N N N N N N N N N N N N ]
[N N N N N N N N N N N N N N N N N ]
[N N N N N N N N N N N N N N N N N ]
[N N N N N N N N N N N N N N N N N ]
[N N N N N N N N N N N N N N N N N ]
[N N N N N N N N N N N N N N N N N ]
[N N N N N N N N N N N N N N N N N ]
[N N N N N N N N N N N N N N N N N ]

4) Actions:

    a) Grid.solve(): take all Pieces ---> matrix
        A: heapify the list of pieces -> binary max heap
        B: take the first piece off of heap (corner), place it - coords
        C: WHILE GAME ON - keep placing pieces:
            a) take coords of last placed --> get the Piece from the matrix
            b) iterate over the rest of unplaced pieces
                - check if that piece has any edge <--> an edge of current piece
                - if yes: map other_edge ---- edge of current piece
                - piece of other_edge --> place on matrix, using edge.size of current_piece
                - recurse(coords of the other_edge.piece)
            c) 
"""
