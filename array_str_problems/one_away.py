"""
One Away: There are three types of edits that can be performed 
on strings: 

- insert a character, 
- remove a character, or 
- replace a character. 

Given two strings, write a function to 
check if they are one edit (or zero edits) away.

EXAMPLE
aple, ple -> true 
^    ^
pales, pale -> true 
pale, bale -> true
pale, bake -> false

balck, black

1. Restate:
- given two strings, return a bool

2. Clarifying Questions:
- is it case sensitive? yes
- can we assume anything about types of characters? no
- could we have an empty string? yes
- is the input mutable? yes
- cannot swap letters in one string to match the other

3. Brainstorming

Intuition:
- should be able to try out all 3 edits on each char of first string
- and then see afterwards if it equals the second string

- Approach:
- use dp
- return True as soon as one succeeds
- use helper funcs for each of the insert, remove, and replace operations

DP TABLE

___|_""_|___"p"__| "a"__|__"l"__|__"e"__|_
""   T      T
"b"
"a"
"l"
"e"

1. Brute Force: --> Quadratic time, can be linear space
- assert that strings are != + within 1 char of being same length
- iterate over shorter (or the first string), keep a pointer in next string
    - modify the string in 3 ways
    - see if it matches the 2nd after each
        - if yes --> True
        - if not move to the next
    - DONT let changes persist between iterations!

insert - take the current index in other string, push all other letters in
selected string down
replace - swap out letter in selected, for one in the other
remove - one index

"""
from typing import List


class Solution:
    def is_close_equal_size(self, str1: List[str], str2: List[str]) -> bool:
        """in this solution we keep the lengths of strings static, so they
        so should already be equal by a signle replacement operation
        """
        # count number of corresponding letters
        count = 0
        for index in range(len(str1)):
            if str1[index] == str2[index]:
                count += 1
        # see if we have at least n-1 chars equal
        return count >= len(str1) - 1

    def is_close_different_size(self, str1: List[str], str2: List[str]) -> bool:
        """in this step it's ok to modify the length of strings,
        (b/c we're adding or removing), so we first need to make sure
        the string characters we do have are in some sort of order
        """
        # sort the lists (chars are in what should be corresponding positions)
        str1.sort()
        str2.sort()
        # find the shorter list
        shorter_length = min([len(str1), len(str2)])
        # count the number of corresponding characters
        count = 0
        for index, char1 in enumerate(str1):
            if index < len(str2) and char1 == str2[index]:
                count += 1
            elif index == len(str2):
                break
        # check if we could make the strings equal
        return count == shorter_length

    def is_close(self, str1, str2) -> bool:
        """
        Time: loglinear
        Space: linear
        """
        # guard clauses
        is_close = False
        if abs(len(str1) - len(str2)) <= 1:
            # put strings into lists
            str1_list, str2_list = list(str1), list(str2)

            if (
                # check for one edit away on equally-sized strings
                (
                    len(str1) == len(str2)
                    and self.is_close_equal_size(str1_list, str2_list)
                )
                or
                # check for one edit away on strings 1 char away in sizes
                (
                    len(str1) != len(str2)
                    and self.is_close_different_size(str1_list, str2_list)
                )
            ):
                is_close = True
        return is_close


if __name__ == "__main__":
    input_cases = [
        # true - same size
        ("bale", "pale"),
        ("", ""),
        # true - different size
        ("pale", "pales"),
        # false - same size
        ("bake", "pale"),
        # false - different size
        ("tac", "cat"),
        ("Spider-Man", "Batman"),
    ]

    sol = Solution()
    for str1, str2 in input_cases:
        is_close = sol.is_close(str1, str2)
        print(f"{str1} and {str2}: {is_close}")
