"""
CtCi 7.8: Design Othello

Othello is played as follows: 
Each Othello piece is white on one side and black on the other. 
When a piece is surrounded by its opponents on:

    1) both the left and right sides, or 
    2 both the top and bottom, 
    
    THEN it is said to be captured and 
         its color is flipped. 
    
On your turn, you must capture at least one of your opponent's pieces. 
The game ends when either user has no more valid moves. 
The win is assigned to the person with the most pieces. 

Implement the object-oriented design for Othello.

1) Scope ---> in nb: https://youtu.be/jlll7wfEKaI
2) Core Objects:
    a) GameBoard: where the pieces go
        - Property 2D matrix (8x8) --> START OFF HERE
            - space_value:
                - null - if there's no piece there
                - Piece object (pter)
        - Class Method: --> (input 2 Player objects)
            game starts, and 
            we init 2 pieces for both players (in the center)
        - Class Method play_game(2 Player) 
        - instance Method: capture_pieces()
            - TODO: decide how to change the colors of "captured piece"
            - TODO: get counts of new # of W and B pieces {W: 14, B: 45}
    b) Piece: can be one of two colors, coords (x, y)
        - current_color: 0 = white, 1 = black
        - current_coords: [-1, -1] to start
    c) Player: agent the game
        - num_pieces
        - ASSIGNED_COLOR = W or B
        - choose_move(gb.board)  # get the coords where the player wants to move next

3) Relationships: SKIP

4) Method: ABOVE

5) Approach:

GameBoard.play_game(player1, player2):

    A: start_game:
        1) make a new GB instance --> gb init'd w/ an 8x8 grid of null values
        2) assign colors to players
        3) init the board w/ two pieces for each player (increment their num_pieces)
    B: game_loop:
        1) should_continue = True
        2) randomly choose a player to take first turn --> active_player
        3) while should_continue:
            a) coords = active_player.choose_move(gb.board) 
            b) place the piece (using active player's color, and given coords)
            c) piece_counts = gb.capture_pieces() accordingly (capture any pieces)
            d) update the num_pieces of the active_player and other_player
            e) swap active_player and other_player
            f) should_continue = check if other_player has moves remaining (aka board.is_valid())
        4) declare the winner
        5) ask to restart

            

"""