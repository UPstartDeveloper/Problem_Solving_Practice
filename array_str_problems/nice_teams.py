#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skillLevel
#  2. INTEGER minDiff
#


def maxPairs(skill_levels, min_diff):
    """
    unsorted array of integers
    pos integers
    dupes
    at least 1 int

    minDiff is a non negative int

    return # of pairs where diff >= minDiff

    Clarifications:
    possibilities - no duplicating values in pairs
    skillLevel list is MUTABLE

    Intuition:
        permutations problem

    Edge Cases:
        negatives = not going to worry about it
        float = raise ValueError

    Approaches:
    1. Brute force - try every combo, increment if it works
        A) quadratic, constant space

    2) use a set
        ratings = [1, 2, 3, 4, 5, 6], mD = 4
                   ^           ^
        A: put all the elems in a set
        B: iterate over elems
            a) look for an element at least bigger than mD

    3) Sorting
    1, 1, 2, 3, 4, 5
        a) [1, 2, 3, 4, 5, 6], mD = 4
            ^              ^

    4) Set + Sort it
        A: init a set
        B: sort the elems
        C: iterate w/ 2 pters
            a) start at beginning
            b) calc the pair = elem + mD
            c) iterate from back --> find lowest elem that meets
            d) if found - increment pair_count, add index to set
        D: return pair_count

    [3, 4, 5, 2, 1, 1], mD = 3

    indices_used = {
        4, 5
    }
     0  1  2  3  4  5
    [1, 1, 2, 3,  ,  ]
     ^           ^
        ^          ^
           ^
     1 + mD = 4

     pC = 0, 1, 2

    """
    # A: init a set
    used = set()
    pairs = 0
    # B: sort the elems
    skill_levels.sort()
    # C: iterate w/ 2 pters
    first_player = 0
    # a) start at beginning
    while first_player < len(skill_levels):
        if first_player not in used:
            # b) calc the pair = elem + mD
            first_skill = skill_levels[first_player]
            threshold = first_skill + min_diff
            # c) iterate from back --> find lowest elem that meets
            second_player = len(skill_levels) - 1
            if skill_levels[-1] >= threshold:
                while second_player > first_player:
                    second_skill = skill_levels[second_player]
                    # d) if found - increment pair_count,
                    if second_skill >= threshold:
                        # make sure we can't go back further
                        skill_before = skill_levels[second_player - 1]
                        before = second_player - 1
                        if (skill_before < threshold) or before in used:
                            if second_player not in used:
                                # add index to set
                                used.add(second_player)
                                pairs += 1
                                # break this loop
                                break
                    # otherwise keep looking
                    second_player -= 1
        # e) move on to next index
        first_player += 1
    # D: return pair_count
    return pairs


if __name__ == "__main__":
    pass
