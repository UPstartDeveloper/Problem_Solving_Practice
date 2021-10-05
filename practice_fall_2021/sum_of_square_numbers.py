class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Link to problem: https://leetcode.com/problems/sum-of-square-numbers/

        Input/Problem:
            - 1 non neg int
            - reverse eng PythagThm
            - unsigned 32 bit int
            - we know the addends <= c

        Edge Case:
            0? ---> true or false? assume false
            a != b required? assume not required

        Approach:
            A: generate array of all squares <= c (start at 0)
            B: check if any square == c / 2 ---> return True
            C: two pter to find if pair exists (if <, increase left, else right-=1 )
                - stop when left > right or sum > c

        Test Cases:

        1) 0: ✅

        [0]

        2) 17 ✅

        [0, 1, 4, 9, 16]
         ^            ^

        3) 25: ✅

        4) 24:

        [0, 1, 4, 9, 16]
                   ^
                      ^
        """

        def _generate_squares():
            squares = []
            root = 0
            while root * root <= c:
                squares.append(root * root)
                root += 1
            return squares

        def _is_pair(squares):
            # stop when left > right or sum > c
            left, right = 0, len(squares) - 1
            while left <= right:
                pair_val = pv = squares[left] + squares[right]
                if pv > c:
                    right -= 1
                elif pv == c:
                    return True
                elif pv < c:
                    left += 1
            return False

        # A: generate array of all squares <= c (start at 0)
        squares = _generate_squares()
        # B: two pter to find if pair exists (if <, increase left, else right-=1 )
        return _is_pair(squares)
