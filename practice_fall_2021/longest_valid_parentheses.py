class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
                Leetcode: https://leetcode.com/problems/longest-valid-parentheses/

                Input/Problem:
                    - ASSUME stirng fits in RAM
                    - ASSUME input is immutable
                EC:
                    1) no chars --> 0
                    2) TODO

                Intuitive:
                    Stepping:
                        1) validating a string --> T/F
                        2) len()
                        2) max out the lengths

                Approaches:

                    1) Brute Force - n^3
                        # A: init max_length = 0
                        # B: try all the substrs
                            # C: validate it
                            # D: if T--> compare w/ max
                        # E: return max_length

                    2)

                0   1   2   3   4   5
                )   (   )   (   )   )
        ndx             ^
        ans     0   0   2
        start       ^

        # @ each index:
            choice - do we cont. the longest valid substring before?
                   - start a new substring?


                max(len(valid substr ending at that index), max_length)?

        """
        ### HELPERS
        def _validate(start, stop) -> bool:
            """ASSUME string starts w/ opening parens )("""
            ndx, num_unclosed_open, num_extra_closing = start, 0, 0
            while ndx < stop + 1:
                char = s[ndx]
                if char == "(":
                    num_unclosed_open += 1
                elif char == ")" and num_unclosed_open > 0:
                    num_unclosed_open -= 1
                elif char == ")":
                    num_extra_closing += 1
                # move
                ndx += 1
            return (num_unclosed_open == 0) and (num_extra_closing == 0)

        ### DRIVER
        # EC
        if s == "":
            return 0
        # BF
        max_length = 0
        # B: try all the substrs
        start = 0
        while start < len(s):
            if s[start] == "(":
                stop = start + 1
                while stop < len(s):
                    # C: validate it
                    is_valid = _validate(start, stop)
                    # D: if T--> compare w/ max
                    current_length = stop - start + 1
                    if is_valid and current_length > max_length:
                        max_length = current_length
                    stop += 1
            # increment
            start += 1
        # all done!
        return max_length


"""
s = "(()"
      ^^
       

ml = 0, 2

"""
