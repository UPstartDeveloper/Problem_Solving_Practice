class Solution:
    """https://neetcode.io/problems/climbing-stairs"""
    def climbStairs(self, n: int) -> int:
        """
        Input(s):
            n: int
                pos int
                immutable
                represents a distance we need to traverse

        Outputs:
            int: # of unique "paths" to n
                paths = ordered sequence of 1's/2's

        Intuition:
            DP

        Constraints:
            the path we take
                --> sequence must EXACTLY sum to n

        Assumptions:
            EC: n <= 1 --> N/A
                if so --> return 0 or ValueError

        Approach:

            1. DP
                top down?
                    subproblem: num_paths_from_position
                        input: current_pos

                        base case:
                            n >= current_pos:
                                return 0

                        recursive case:
                            n < current_pos:
                                return (
                                    num_paths_from_position(current_pos + 1) +
                                    num_paths_from_position(current_pos + 2)
                                )

                    complexity
                        time: O(2 * n), w/o memoization
                            w/ memoization --> gets closer to O(n), but need to confirm
                        space: O(n)

        sf              n           current_position    ret_val
        1               2           0                   2
        2               2           0 + 1 = 1           0
        3               2           1 + 1 = 2           1
        4               2           1 + 2 = 3           0
        5               2           0 + 2 = 2           1

                bottom up

                    DP table

                        0   1   2.   3.  4.  5.  6 .... n --> X

                        let's say n = 7

                        init an array of n + 2 spaces?
                            idea --> each arr elem = sub proble
                            traverse in reverse
                                base case:
                                    last index = 0
                                    second to last = 1
                                recursive case:
                                    answer = sum of two elems to the right?

                        test
                            n = 2
                            [0, 0, 0]
                            [0, 0 + 1 = 1, 0]
                            [0 + 1 + 0 + 1 = 2, 0 + 1 = 1, 0]

                            [
                                2,
                                1,
                                1,
                                0
                            ]

                            n = 3
                            [
                                0, = 4
                                0, = 2
                                0, = 1
                                0 = 0
                            ]

                            [
                                0, >> 3
                                0, >> 2
                                0, >> 1
                                0,>>> 1
                                0 --> 0
                            ]

        """
        ### HELPER(S)
        def _init_cache():
            self.cache = dict()

        def _optimal():
            """
            Bottom up DP - O(n) time, O(1) space
            np = 0, 1, 2
            a1 = 1, 1, 2
            a2 = 0, 1, 1
            a3 = 1, 2

            iter
            1, 2
            """
            num_paths = 0
            addend1, addend2 = 1, 0

            for _ in range(n):
                num_paths = addend1 + addend2
                addend2 = addend1
                addend1 = num_paths

            return num_paths

        def _num_paths_from_position(current_position: int) -> int:
            # base case: we're at/beyond the end
            if current_position not in self.cache:
                if current_position == n:
                    self.cache[current_position] = 1
                elif current_position > n:
                    self.cache[current_position] =  0
                # recursive case: we're en route to the top of the stairs
                else:  # n < current_pos
                    self.cache[current_position] = (
                        _num_paths_from_position(current_position + 1) +
                        _num_paths_from_position(current_position + 2)
                    )
            return self.cache[current_position]

        ### DRIVER
        if n < 1:
            return 0

        # _init_cache()
        # return _num_paths_from_position(0)

        return _optimal()
