class Solution:

    TEST_CASES = [
        # input, exp. output
        ("10[a]", "aaaaaaaaaa"),
        ("3[abc]4[ab]c", "abcabcabcababababc"),
        ("2[3[a]b]", "aaabaaab"),
    ]

    def decompress(self, compressed: str):
        # A: init list for global output
        decomp_strs = list()
        # B: traverse the string
        global_index = 0
        while global_index < len(compressed):
            next_char = compressed[global_index]
            # C: single character seen
            if next_char.isalpha() is True:
                decomp_strs.append(next_char)
                global_index += 1
            # D: assuming a number - compressed substring starts
            elif next_char != "]":
                # calculate the no. of reps
                start_num = opening_bracket_index = global_index
                while compressed[opening_bracket_index] != "[":
                    opening_bracket_index += 1
                reps = (
                    compressed[start_num:opening_bracket_index]
                )
                reps = int(reps)
                # compute the substring 
                subproblem_str = (
                    compressed[opening_bracket_index + 1:]
                )
                substring_unit, bracket_length = self.decompress(subproblem_str)
                # E: multiply the substring, and add it to output
                substring_complete = [substring_unit for _ in range(reps)]
                decomp_strs.append("".join(substring_complete))
                # F: update global index to the start of the next subproblem
                global_index = opening_bracket_index + bracket_length + 1
            # G: form final output
            else:  # next_char == "]"	
                return "".join(decomp_strs), global_index + 1
        # H: also return decompressed string, if global output
        return "".join(decomp_strs)

    
if __name__ == "__main__":
    sol = Solution()
    # run the test cases
    for input, exp_output in sol.TEST_CASES:
        actual_output = sol.decompress(input)
        assert actual_output == exp_output, f"Expected: {exp_output}, returned {actual_output}"
        print(input, "✅")
