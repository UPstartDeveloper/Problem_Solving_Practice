"""
def set_letters(haystack, needle, needle_index, haystack_index):
    needle_letter, haystack_letter = (
    needle[needle_index], haystack[haystack_index]
    )
    return needle_letter, haystack_letter

def strStr(haystack, needle):
    # init a variable tracking the index of where the match begins
    match_start = 0
    # iterate over the letters of the haystack
    haystack_index = 0
    while haystack_index < len(haystack):
        # compare each letter with the first of the needle
        needle_index = 0
        needle_letter, haystack_letter = (
            set_letters(haystack, needle, needle_index, haystack_index)
        )
        # if equal, make sure it's a full match
        while needle_index < len(needle) and needle_letter == haystack_letter:
            # compare each consecutive letter of needle, to consecutive in haystack
            needle_letter, haystack_letter = (
                set_letters(haystack, needle, needle_index, haystack_index)
            )
            needle_index += 1
            haystack_index += 1
        # if it's a full match, return the start index
        if needle_index == len(needle):
            return match_start
        # if it turns out not a full match, then we increment start by one
        match_start += 1
        haystack_index = match_start
    # needle not found
    return -1
"""
"""
# This is Abhishek Kulkarni's solution, I have pasted it here to compare
# with the one I have above
def strStr(haystack: str, needle: str):
    # handles cases where needle is empty, or haystack is identical to needle
    if needle == haystack or needle == "":
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
"""
"""
def strStr(haystack, needle):
    # early exit: needle is empty string
    if needle == '':
        return 0
    # init the match at -1
    # match = -1
    # find where a letter of hs, matches the first letter of needle
    hs_idx = 0
    while hs_idx < len(haystack):
        n_idx = 0
        # if it does
        if haystack[hs_idx] == needle[n_idx]:
            # copy over the hs_index into another variable
            h_match = hs_idx
            # iterate hs using the hs_index, and needle using n_idx
            while n_idx < len(needle) and h_match < len(haystack):
                if needle[n_idx] == haystack[h_match]:
                    n_idx += 1
                    h_match += 1
                else:
                    break
            # if hit the end of n_idx before end of hs, then return match_start
            if n_idx == len(needle):
                return hs_idx
        # reset match_start to -1
        # increment hs_index
        hs_idx += 1
    # return match_start
    return -1
    """

def strStr(haystack, needle):
    # early exit
    if needle == '':
        return 0
    # iterate backwards through the haystack
    for hs_idx in range(len(haystack) - len(needle), 0, -1):  # h - n iteration
        # compare the substring of haystack to needle
        if haystack[hs_idx:hs_idx+len(needle)] == needle:  # n iterations
            return hs_idx
    # match not found
    return -1

    # Time: linear - O(n(h - n)) --> O(hn)
    # Space: O(n)


if __name__ == '__main__':
    print(strStr("aaaaaaaaaaa", "aaaaaaaaaab"))
"""
     0   1   2  3  4 
     h   e   l  o  o
0 l. F.  F   T  
1 l.            T
  
"""
