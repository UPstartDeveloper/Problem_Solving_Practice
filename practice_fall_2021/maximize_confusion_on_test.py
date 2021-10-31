class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        Leetcode Link: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

        Input/Problem:
            non-emptpy string
            mutable
            k -- 1 to n

        Problem - optimmize for most repeated chars

        EC:
            1) empty string
            2) string that's too large
            3) when multiple repeated sequences
            4) alternating letters
            5) solution is "non-greedy" - it's better to change in one direction,

                TTTTTTTTTTT, k = 0

                k = 0
                TTTTTTTTTTTTFF
                ^       ^

        Intuition:
            dynamic programming

        Approach:
            1) given an array of char -> return the length of longest repeated sequnce
            2)

        1) Brute:
            A: make all the possible changes (to consecutive repeated letters)
            B: find the longest after each of them

        2) Greedy Solution:
            A: find the length of longest repeated seq
            B: locate the index of 1st seq w/ the length
            C: transformations
                c) move left and right - see what answer is
            D: return the answer


        Example:

            <-  ->
        aK = TTTTTTTT
               ^  ^
             ^^
        k = 2
            1
            0

        """
        ### HELPER
        def _locate_longest_repeated(string):
            """linear sesch for the longest length"""
            longest_len = float("-inf")
            longest_seq_start = -1
            s = starting = 0
            # find all the repeated seq's
            while s < len(string):
                # see how the len(string) repeated seq is
                repeated_len = 1
                next_ndx = nn = s + 1
                while nn < len(string) and string[s] == string[nn]:
                    repeated_len += 1
                    nn += 1
                # update the longest (length and index) as needed
                if longest_len < repeated_len:
                    longest_len = repeated_len
                    longest_seq_start = s
                # update the starting index
                s = nn
            # all done!
            return longest_len, longest_seq_start

        def _transform(length, index, direction="both"):
            """0.   1.   2.   3
            ic = # ['T', 'T', 'F', 'F']
            s   e
            0   1

            ct
            """
            input_chars = ic = list(answerKey)  # ['T', 'T', 'F', 'F']
            # A: calculate endpts of the longest repeated sequence
            start, end = index, (index + length) - 1  # 0 + 1 - 1 = 0
            # keep track of T->F or F->T
            change_to = ic[start]
            # B: for left:
            ops_left = k
            left_runner = start - 1
            # try as make k operations in total, avoid index errors
            if direction != "right":
                while left_runner > -1 and ops_left > 0:
                    # ensure that letters are actually changed
                    if ic[left_runner] != change_to:
                        ic[left_runner] = change_to
                        ops_left -= 1
                    left_runner -= 1
            # C: do same  for right
            if direction != "left":
                right_runner = end + 1  # 0 + 1 = 1
                while right_runner < len(ic) and ops_left > 0:
                    if ic[right_runner] != change_to:
                        ic[right_runner] = change_to
                        ops_left -= 1
                    right_runner += 1
            # C: return a new string
            return "".join(ic)

        ### DRIVER
        # A&B: find the length of longest repeated seq, where it starts
        # TODO: make sure this is done for whatever letter is the majority, globally speaking, in the string
        init_length, index = _locate_longest_repeated(answerKey)
        # C: try 3 kinds of  transformations
        transformed_str1 = _transform(init_length, index, direction="left")
        transformed_str2 = _transform(init_length, index, direction="right")
        transformed_str3 = _transform(init_length, index, direction="both")
        # D: return the answer
        longest_poss = 0
        strings = [transformed_str1, transformed_str2, transformed_str3]
        for string in strings:
            output_len, index = _locate_longest_repeated(string)
            if output_len > longest_poss:
                longest_poss = output_len
        return longest_poss
