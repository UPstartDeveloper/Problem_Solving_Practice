from typing import List

class Solution:
    # init is_found, and a stack, a visited set
    def __init__(self):
        self.is_found = False 
        self.visited = set([])
        self.DIRECTIONS = {
            "right": (0, 1),  # right
            "left": (0, -1),  # left 
            "down": (1, 0),  # down
            "up": (-1, 0), # up
        }
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        is looking for the next letter case sensitive, or
        should I just not care about different cases?
        
        "adjacent" cells are horizontally or vertically neighboring
        
         The same letter cell may not be used more than once.
         
         are we allowed to edit the cells in the grid? (assume not)
         
         Assume the board is rectangular
         
         board and word consists only of lowercase and uppercase English letters.
         - so I'll assume the function is case sensitive
         
         word = SpiderMan
         board = [
             s p i d e
             g n a m r
         ] ==> False? 
         
         intuition: 
         - use a graph DFS to find a path
         - each letter in the grid is a vertex
         - can have up to 4 neighbors 
         - we want to find a path between starting letter to end
         
         edge cases:
         - what if I find non alphabetic characters? - don't add to the stack
         - what if the grid is empty --> return False
         
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
         ], 
        
        word = "ABCCED"
                ^
         
         approach:
         # A: check the grid to make sure it's not empty
            # B: init is_found, and a stack, a visited set, and a pointer in the word
            # C: DFS the grid
                # iterate over the indices of the grid
                    # check if the letter is the first letter in the word
                    # if it is, check the unvisited neighbors of the node
                        - if it matches the next letter, push it onto the stack
                        - if we reach the last letter and match, return true
                    # if no matches (or the first node doesn't match) - then move one
         # return the is_found value
        """
        def check_letter_mutative(row_index, col_index, word_index):
            # get the letter from the board
            board_letter = board[row_index][col_index]
            # add this node to the visited set
            # self.visited.add((row_index, col_index))
            board[row_index][col_index] = "0"
            # get the letter from the word
            word_letter = word[word_index]
            # print(f"At board letter: {board_letter} at {(row_index, col_index)}")
            # print(f"checking against word letter: {word_letter} at {word_index}")
            # print(f"Visited so far: {self.visited}")
            # if matching,
            if word_letter == board_letter:  
                # if matching the end, return True
                if word_index == len(word) - 1:
                    self.is_found = True
                # push the neighbors 
                else:  # (if not in the end)
                    for direction in self.DIRECTIONS:
                        # calculate the coordinates of the neighbor to check next
                        delta_row, delta_col = self.DIRECTIONS[direction]
                        # print(f"Going {direction} from {(row_index, col_index)}")
                        next_row, next_col = (row_index + delta_row, col_index + delta_col)
                        # validate that we can go here
                        if 0 <= next_row < len(board) and 0 <= next_col < len(board[next_row]):
                            # if (next_row, next_col) not in self.visited and board[next_row][next_col] == word[word_index + 1]:
                            if board[next_row][next_col] == word[word_index + 1]:
                                # traverse the next node
                                check_letter_mutative(next_row, next_col, word_index + 1) 
                                # in case that route didn't help, remove
                                # self.visited.remove((next_row, next_col))
            board[row_index][col_index] = board_letter
        def check_letter_immutative(row_index, col_index, word_index):
            # get the letter from the board
            board_letter = board[row_index][col_index]
            # add this node to the visited set
            self.visited.add((row_index, col_index))
            # get the letter from the word
            word_letter = word[word_index]
            # print(f"At board letter: {board_letter} at {(row_index, col_index)}")
            # print(f"checking against word letter: {word_letter} at {word_index}")
            # print(f"Visited so far: {self.visited}")
            # if matching,
            if word_letter == board_letter:  
                # if matching the end, return True
                if word_index == len(word) - 1:
                    self.is_found = True
                # push the neighbors 
                else:  # (if not in the end)
                    for direction in self.DIRECTIONS:
                        # calculate the coordinates of the neighbor to check next
                        delta_row, delta_col = self.DIRECTIONS[direction]
                        # print(f"Going {direction} from {(row_index, col_index)}")
                        next_row, next_col = (row_index + delta_row, col_index + delta_col)
                        # validate that we can go here
                        if 0 <= next_row < len(board) and 0 <= next_col < len(board[next_row]):
                            if (next_row, next_col) not in self.visited and board[next_row][next_col] == word[word_index + 1]:
                                # traverse the next node
                                check_letter_immutative(next_row, next_col, word_index + 1) 
                                # in case that route didn't help, remove
                                self.visited.remove((next_row, next_col))        
        # A: check the grid to make sure it's not empty
        if len(board) > 0 and len(board[0]) > 0:
            # C: DFS the grid
            word_index = 0
            for row_index, row in enumerate(board):
                for col_index, board_letter in enumerate(row):
                    # check if the letter is the first letter in the word
                    word_letter = word[word_index]
                    # traverse from this board vertex
                    self.visited = set([])
                    if board_letter == word_letter:
                        check_letter_mutative(row_index, col_index, word_index)
                        # exit early if the word found
                        if self.is_found is True:
                            return self.is_found
                        # else:
                            # self.visited = set({})
        # return the is_found value
        return self.is_found
"""
board = 

[
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
word = "ABCESEEEFS"
w_idx =    ^
----------------------------------------------
board = 
[
       0   1   2   3
 0   ["A","B","C","E"],
 1   ["S","F","C","S"],
 2   ["A","D","E","E"]
]

word = "SEE"
w_idx = ^

is_found = False 
visited = {
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3)
}

DIRECTIONS = [
    (0, 1)  # right
    (0, -1),  # left 
    (1, 0),  # down
    (-1, 0), # up
]

r_idx = 1,
c_idx = 3,

nr = 0
nc = 0
------------------------------
 board = [
      0   1   2   3
0   ["A","B","C","E"],
1   ["S","F","C","S"],
2   ["A","D","E","E"]
], 
        012345
word = "ABCCED"
w_idx =   ^
is_found = False 
visited = {
    (0, 0),
    (0, 1),
}
DIRECTIONS = [
    (0, 1)  # right
    (0, -1),  # left 
    (1, 0),  # down
    (-1, 0), # up
]

r_idx = 0, 0, 0
c_idx = 0, 1, 2

nr = 0, 0
nc = 1, 2



"""
            

if __name__ == "__main__":
    """board = [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ]
    word = "ABCESEEEFS"""

    board = [["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","b"]]
    word = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"  
    sol = Solution()
    print(sol.exist(board, word))                     