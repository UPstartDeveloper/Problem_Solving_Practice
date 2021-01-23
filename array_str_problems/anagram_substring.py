# Problem: Given two strings, str_a and str_b, determine whether any anagram of str_b, 
# occurs as a substring of str_a.
# Constraints: Comparison is NOT case sensitive and input string sizes vary 
# Examples: 
# 1) Here come dots and lines that helped build America, The Morse Code ->True
# 2) crowd, word -> True
# 3) There is no anagram here, some word -> False
# 4) There is no anagram here, game -> False

# Explanations:
#TRUE = Some arrangement of the characters in str_b is a substring in string a
#FALSE = Some arrangement of the characters in stb_b is NOT a substring in string #a. No re-arrangement of characters in str_b are contiguously found in str_a.


"""
Assumptions: 
length of string A is always same or greater as that of str_b
str_a and str_b only contain lower/uppercase English letters
case insensitive
spaces do count
remember - substrings are continguous

Edge Cases: 
length of b > a --> return False right away
a or b is empty, or null

Intuition:
- how to tell if two equally sized string (w/ only letters) are anagrams
    - make sorted lists of both, see if they are equal (n log n time, n space)
    - make frequency distributions (linear time and space)

Approach:
# make a freq dist of str_b
# compare the freq_dist of b, to that of substrings of a (equal size)
    # if it works, return T
# if none possible --> return False

Finding Out Anagrams:

1. Freq Dist:
    - linear time 
    - linear space

2. Sorting
    - loglinear time
    - linear space
"""


def has_anagram_substring(a: str, b: str) -> bool:

    def make_freq_dist(string: str) -> dict:
        dist = dict()
        for letter in string:
            letter = letter.lower()
            if letter not in dist:
                dist[letter] = 1
            else: 
                dist[letter] += 1
        return dist

    def is_anagram(sub_a, b) -> bool: 
        # make a freq dist of str_b
        b_dist = make_freq_dist(b)
        # make a's freq dist
        a_dist =  make_freq_dist(sub_a)
        # compare the freq dist's
        for letter in b_dist:
            if letter not in a_dist or a_dist[letter] != b_dist[letter]:
                return False
        return True

    # edge cases:
    if not a or not b:
        return False
    if len(b) > len(a):
        return False
    # compare the freq_dist of b, to that of substrings of a (equal size)
    start, end = 0, len(b)
    while start <= len(a) - len(b):
        # find the substring of a
        sub_a  = a[start:end]
        # if it works, return T
        if is_anagram(sub_a, b): 
            return True
        # if not, move on to the next substring
        start += 1
        end += 1
    # if none possible --> return False
    return False


if __name__ == "__main__":
    strings =  [
        ("Here come dots and lines that helped build America", "The Morse Code"),
        ("crowd", "word"),
        ("There is no anagram here", "some word"),
        ("There is no anagram here", "game")
    ]
    for str_a, str_b in strings:
        print(has_anagram_substring(str_a, str_b))
