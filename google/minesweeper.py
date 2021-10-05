"""
Minesweeper - goal is to find where all "mines" are

9 = mine
non-mine - give the num (int) of mines in adj squares (0-8)
- up, down, left, right, upper-left, upper-right, lower-right, lower-left

Example Input:

0  0  0  0  0      [ - - - - - ]
0  0  0  0  0   
1  1  1  0  0
1  9  1  0  0
1  2  2  1  0
0  1  9  1  0
0  1  1  1  0

Matrix object
    - 2D List of integers
    - supports resize(rows, cols), 
               get(row, cols),
               rows() - get the rows
               cols() - get the colummns

Clarifications:

Lose - find a 9 cell
Win - is if num of hidden cells rem == no of mines
     

1. Intution: What does gameplay look like?
    A: Construct the matrix - 
        - being given the number of mines
        - dims of matrix
        - mmake a "hidden matrix" that is given to user
    B: One TURN: enter the game loop
        - print the current state of the hidden matrix
        - prompt the user to choose a cell
        - un-hide that cell
            - if it's mine (9) --> game over
            - if it's 0 --> BFS until we hit a non-zero level
            - otherwise - just reveal that cell (hidden)
        - update the hidden matrix
        - check if the user has won --> end the game loop
    C: propmt the user to play again

2. Approach:

0 0 0-------   0 0
----0 -----
----------
----------
----------
    

class Game:
    - 1 matrix answer_key --> what each sq actually contains
    - 1 matrix game_board --> player sees, starts off hidden "-"

    - def constructMatrix(rows, cols, # mines):
        - Set(Tuples(int)) - generate randommly the coords of mines should be 
        - instantiate the matrix
        - place the mines in the coords (9)
        - iterate over each cell, label it
            - use # 9's we find in that 1st of adj cells

        - make the matrix the player sees

    - def playGame(answer_key, player_matrix):
        while True:
            prompt the user to choose a sqaure
            get the value at those coords in answer_key
            update the same square in player matrix
            decide what to do next 
                1-8 - do nothing else
                0 - BFs to revela up to first level of non-zero
                9 - game over
            print the updated board back to user
            decide if player has won ---> if so, end the loop, print ("You Win")
            otherwise, cont. loop with a dff. message 
                not 9 - "pick another cell"
                9 - "sorry you lose"
             

    - def gameLoop(rows, cols, # of mines)
        - main function
        - A: prompt the user if they want to start/restart a game
            - B: constructMatrix- make the matrices for the answer, and player
            - C: playGame

3. Edge Cases:
    - rect. matrix?
    - ASSUME no. sq > no. mines
    - ASSUME no empty matrix
    - ASSUME the matrix can fit in memory
    - ASSUME in between turns, all the unhidden cells != mines


    
"""
import random
from collections import deque


class Game:

    HIDDEN_CHAR = "-"

    DIRECTIONS = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (1, 1),  # bottomm right
        (1, -1),  # bottom left
        (-1, 1),  # up-r
        (-1, -1),  # up-l
    ]

    def __init__(self):
        self.answer = []
        self.grid = []
        self.mines = self.hidden = 0

    def _label_other_squares(self):
        # use # 9's we find in that 1st ring of adj cells
        for row_index, row in enumerate(self.answer):
            for col_index, value in enumerate(row):
                adj_mines = 0
                for diff_row, col_diff in self.DIRECTIONS:
                    # find the coords of neighbor
                    nr = neighbor_row = row_index + diff_row
                    neighbor_col = col_index + col_diff
                    # check if coords in the grid
                    if 0 <= neighbor_row < len(self.answer):
                        if 0 <= neighbor_col < len(self.answer[nr]):
                            # if it's a mmine, inccreent count ++
                            neighbor = self.answer[nr][neighbor_col]
                            if neighbor == 9:
                                adj_mines += 1
                # update the grid
                self.answer[row_index][col_index] = adj_mines

    def construct_matrix(self, rows, cols, mines):
        # init the answer matrix
        for index in range(rows):
            self.answer[index] = [-1 for _ in range(cols)]
        # - Set(Tuples(int)) - generate randommly unique coords of mines should be
        mine_coords = set()
        for _ in range(mines):
            row = random.randint(0, len(rows) - 1)
            col = random.randint(0, len(cols) - 1)
            while self.answer[row][col] != -1:
                row = random.randint(0, len(rows) - 1)
                col = random.randint(0, len(cols) - 1)
            # - place the mines in the coords (9)
            self.answer[row][col] = 9
            mine_coords.add((row, col))
        # - iterate over each cell, label it
        self._label_other_squares()
        # - make the matrix the player sees
        for index in range(rows):
            self.grid[index] = [self.HIDDEN_CHAR for _ in range(cols)]

    def _reveal(self, row_choice, col_choice):
        # A: init a queue
        q = deque()
        # B: put in the first item
        q.append((row_choice, col_choice))
        square = self.answer[row_choice][col_choice]
        # C: find the rest of the non-mines
        while square == 0 or len(q) > 0:
            row, col = q.popleft()
            square = self.answer[row][col]
            self.grid[row][col] = square
            if square == 0:
                for diff_row, col_diff in self.DIRECTIONS:
                    # find the coords of neighbor
                    nr = neighbor_row = row + diff_row
                    nc = neighbor_col = col + col_diff
                    # check if coords in the grid
                    if 0 <= neighbor_row < len(self.answer):
                        if 0 <= neighbor_col < len(self.answer[nr]):
                            neighbor = self.answer[nr][nc]
                            if neighbor == self.HIDDEN_CHAR:
                                q.append((nr, nc))

    def is_winner(self):
        """determine if number of hidden sq/== no. of mines"""
        return self.hidden == self.mines

    def play_game(self, answer_key, player_matrix):
        while True:
            # TODO: show the board - self.grid
            # prompt the user to choose a sqaure
            row_choice = int(input("Which row you like?"))
            col_choice = int(input("Which column you like?"))
            # get the value at those coords in answer_key
            unhidden = self.answer[row_choice][col_choice]
            # update the same square in player matrix
            self.grid[row_choice][col_choice] = unhidden
            # 9 - game over
            if unhidden == 9:
                print("sorry you lose")
                break
            # otherwise update the number of hidden cells
            self.hidden -= 1
            # 0 - BFS to revela up to first level of non-zero
            if unhidden == 0:
                self._reveal(row_choice, col_choice)
                print("Good choice! No mines here :)")
            # decide if player has won ---> if so, end the loop, print ("You Win")
            if self.is_winner():
                print("And You Win the Game!")
                break
            # not 9 - "pick another cell"
            elif 1 <= unhidden < 8:
                print("Oooh, be careful! You almost hit a mine!")
        # TODO: show the board - print the updated board back to user one last time

    def game_loop(self, rows, cols, mines):
        """main function"""
        self.mines = mines
        user_response = input("Would you like to start a new game? Enter Y/N")
        should_continue = user_response.upper()[0] == "Y"
        while should_continue:
            self.hidden = rows * cols
            # A: constructMatrix - make the matrices for the answer, and player
            self.construct_matrix(rows, cols, mines)
            # B: playGame
            self.play_game()
            # C: prompt the user if they want to start/restart a game
            user_response = input("Would you like to start a new game? Enter Y/N")
            should_continue = user_response.upper()[0] == "Y"
