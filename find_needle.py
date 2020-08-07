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

if __name__ == '__main__':
    print(strStr("aaaaa", "bba"))
"""
     0   1   2  3  4 
     h   e   l  o  o
0 l. F.  F   T  
1 l.            T
  
"""
