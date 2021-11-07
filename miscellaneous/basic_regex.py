def is_match(text, pattern):
    """Basic Regex Parser that only includes '.' and '*'. Case sensitive."""

    def match(t_char, p_char):
        """Defines the comparision between characters in the text and pattern."""
        if t_char == p_char or p_char == ".":
            return True
        return False

    # Scratch Work
    # . - wildcard, anything you want
    # * - multiple of the preceding charactering
    # Ab*, "Abbb"
    # true
    # only letters
    # case sensitive
    #  text = "aa", pattern = "a"
    #  False => t != p
    # Simple Str Matching
    # ite
    # p "a"
    # ^
    # t = "aa"
    #       ^

    # letters
    # length
    # can also havwe 0 or more instance of * chars

    # Example
    # text = "aa", pattern = "aa" --> T
    # "abc", pattern = "a.c" --> T

    # text = "acd", pattern = "ab*c."  -

    # t = "acd"
    #       ^
    # p = "ab*c."
    #         ^
    # ac, abc, abbc, abbbc, abbbbc

    # t =;
    #        ^
    # p = ;
    # .        ^

    # t = abcdf;
    # s = a.*;
    #
    # Use Recursion?
    # Base Cases
    # . ---> T
    # a --> p_char == t_char
    # Recursive Cases
    # . b*
    # .*
    # text = "acd", pattern = "ab*c."
    #          ^                  ^

    # Pseudocode - 2 pointers
    # init 2 pointers at start of p and t
    p_idx, t_idx = 0, 0
    # iterate over p
    while p_idx < len(pattern):
        p_char = pattern[p_idx]
        # check for an * after the pointer in p
        if p_idx < len(pattern) - 1 and pattern[p_idx + 1] == "*":
            # do a while loop in t to find how many of the pchar we have
            num_p_char_in_text = 0
            while t_idx < len(text) and match(text[t_idx], p_char):
                num_p_char_in_text += 1
                t_idx += 1
            # if that num >= 0, then T, move ahead the p ointer by 2
            if num_p_char_in_text >= 0:
                p_idx += 2
        # if the p_char = ., or P_char == t_char --> True
        elif match(text[t_idx], p_char):
            # move ahead both poiters
            p_idx += 1
            t_idx += 1
        # if both letters != --> False
        elif t_idx >= len(text) or (
            t_idx <= len(text) and pattern[p_idx] != text[t_idx]
        ):
            return False
    # at the end, we should reach the end of both strings
    return t_idx == len(text)


# Time: O(max(t, p)) - where t = length of text, and p = length of the pattern
# Space: O(1)

if __name__ == "__main__":
    # Test Cases
    assert is_match("", "") == True
    assert is_match("aa", "") == False
    assert is_match("bb", "bb") == True
    assert is_match("", "a*") == True
    assert is_match("abbdbb", "ab*d") == False
    assert is_match("aba", "a.a") == True
    assert is_match("acd", "ab*c.") == True
    assert is_match("abaa", "a.*a*") == True
