#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sortedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def sortedSum(a):
    """
    array of ints

    non-desc order = least to greatest

    ASSUME
    all pos ints
    at least 1 int
    dupes are allowed
    a is mutable

    module the answer w/ (10e9 + 7)

    Intuition:
        - iteratively sorting + summing nums, at the end we cum_sum

    Approach:
        1. Sorting Problem:
            - need an array of n spaces
            - insertion sort the array
                - after each iteration, find sum of s(i)
                - add it to the sums array
            - add all the sums together
        2. Math Problem:
            - make a separate sorted array
            - take a look at the distance each int moved

    Edge Cases:
        - all dupe numbers - not a different algorithm necessarily
        - too many nums/too large - return a ValueError

    """

    def insert_next_elem(index):
        index_to_sort = index
        while index_to_sort > 0:
            # sorting
            index_before = index_to_sort - 1
            elem_to_sort = a[index_to_sort]
            elem_before = a[index_before]
            # swap if needed
            if elem_before > elem_to_sort:
                a[index_before] = elem_to_sort
                a[index_to_sort] = elem_before
            # move back further
            index_to_sort -= 1
        return index + 1

    def sum_of_spaces(spaces):
        # init the sum
        sum_spaces = 0
        coef = 1
        # add sum of elems sorted so far
        for index in range(spaces):
            sum_spaces += a[index] * coef
            coef += 1
        # return the sum
        return sum_spaces

    # A: need an array of n spaces
    sums = list()
    # B: insertion sort the array
    index = 0
    while index < len(a):
        # sort the next element into place, increment index
        updated_index = insert_next_elem(index)
        # - after each iteration, find sum of s(i)
        next_sum = sum_of_spaces(updated_index)
        # - add it to the sums array
        sums.append(next_sum)
        # move on to next index
        index = updated_index
    # C: add all the sums together
    return int(sum(sums) % (10e9 + 7))


if __name__ == "__main__":
    pass
