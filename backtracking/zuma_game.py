class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        """
        Zuma Game: from https://leetcode.com/problems/zuma-game/
        
        questions: 
        - can only insert 1 ball at a time? yes
        
        Goal: find the min number of insert operations 
              to remove all balls from table (until it's clear we can't)
        
        Choices:
        - insert a ball from hand onto the table (any position)
           
           
        Input: board = "WRRBBW", hand = "RB"
        Output: -1
        
        Rules:
        - >=3 ball in the same color touching, remove these balls.
        
        Constraints:
        - 5 different colored balls, each has a unique capital letter
            - W, R R, B, W
        - don't need to empty all the balls from our hand
        -  initial row of balls on the table won’t have any 3 or more 
            consecutive balls with the same color.
        - can have multiple sequences of the same color in the same row
            
            
        Brainstorming:
        
        DIY (not minimal)
        - scan over the table
        - need to record of each contiguous string of same colored balls
        - see if any of the colors in the table match those in my hand
        - start from the top of the row
            - calculate the min number of balls to remove the sequence 
            - see if it's in the hand
            - if so, a
         01234567
        b = "WWRRBBWW"
        h = "WRBRW"
        
        table = 
         [
            color, start index, length
            ["W", 1, 2] 
            ["R", 2, 2]
            ["B", 4, 2]
            ["R", 6, 2]
            
         ]
            
        hand = {
            "W": 2, 
            "R": 2,
            "B": 1
        }
        
        solutions = []
        
        Backtracking (not efficient?)
        # A: scan over the table
        # need to record of each contiguous string of same colored balls
        # see if any of the colors in the table match those in my hand
        # using each sequence as a different starting point
            # solve_game()
            # record the number of inserts (or -1) in an array
        # at the end, return the minimum(solutions)
        
        
        Solving a Game (starting index):
        # A: remove the sequence at the start if possible
        # B: while there are still balls in hand and row:
            # go to the middle of the row
            # try to remove if possible (update the row and hand)
        # C: check if row empty, and return inserts if so (or -1)
            
            
        Game 1:
                    Index: 0
                    Inserts: +1, +1
                    Hand:
                    W   R   B
                    2   2   1
                    1       0
                    
                    Table:
                    color, start index, length
                    0            1           2             3
        step 1 +1   ["W", 1, 2]  ["R", 2, 2] ["B", 4, 2]   ["R", 6, 2]
        step 2 +1                ["R", 2, 2] ["B", 4, 2]   ["R", 6, 2]
        step 3                   ["R", 2, 2]               ["R", 6, 2]
        step 4 - done! return 2
            
    """
   