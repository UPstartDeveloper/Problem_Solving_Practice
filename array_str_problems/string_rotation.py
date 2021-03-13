"""
String Rotation: 

Assume you have a method isSubstring which checks 
if one word is a substring of another (assuming it returns a boolean)

Given two strings, s1 and s2, write code to 
check if s2 is a rotation of s1 using only one call to isSubstring 

(e.g.,"waterbottle" is a rotation of "erbottlewat").

Clarifying Questions:
- rotation is the same thing as permutation? yes
- returning a boolean? yes
- so if the strings are equal, does that still count as a rotation?
    - no
- and can we assume that the first string won't be empty? no
    - in that case if the first string is empty ---> assume I can return False
- any kind of character
- isSubstring returns True when the s1 == s2

Intuition:

- Rotation must be:
    - all the same letters 
    - in the same frequencies or chars
    - it cannot be the same string

"waterbottle" is a rotation of 
"waterbottle"
"erbottlewat"

Approach:

1. Dictionary + isSubstring
    - dict use it to check the frequency dist of both strings
    - take the substring in s2 from the first letter of s1, till the end
        - make sure it's not equal, and isSubstring is True ---> TRue
        - any other case --False

Edge Cases:
- empty strings --> False
"""


def is_rotation(s1: str, s2: str) -> bool:
    def isSubstring(s1: str, s2: str) -> bool:
        pass

    def freq_dist(string) -> dict:
        dist = dict()
        for char in list(string):
            if char not in dist:
                dist[char] = 1
            else:
                dist[char] += 1
        return dist

    def is_equal(char_dist1, char_dist2):
        if len(char_dist1) == len(char_dist2):
            return False
        
        for char in char_dist1.keys():
            if char not in char_dist2 or char_dist1[char] != char_dist2[char]:
                return False

        return True
        
    def is_permutation(s1, s2):
        # A: make 2 dict of the char dist
        char_dist1, char_dist2 = freq_dist(s1), freq_dist(s2)
        # B: compare the dicts
        return is_equal(char_dist1, char_dist2)
    
    # validate the input, then check if it's a permutation
    if (s1 and s2) and is_permutation(s1, s2):
        # find the first letter of s1 in s2
        first_letter_s1 = s1[0]
        ndx_first_letter_s2 = s1.find(first_letter_s1)
        # take the substring from there, till the end
        substr_s2 = s2[ndx_first_letter_s2:]
        # check if that != s1
        if s1 != substr_s2 and isSubstring(s1, substr_s2):
            return True
    return False
