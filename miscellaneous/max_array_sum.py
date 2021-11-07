#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    def compute_sum(even=True):
        # get the index to start iterating from
        starting_idx = 0
        if even is False:
            starting_idx = 1
        # get the hgihest sum from combining every other element
        max_sum = 0
        for index in range(starting_idx, len(arr), 2):
            # only add elements that make the sum greater
            elem = arr[index]
            if elem > 0:
                max_sum += elem
        return max_sum

    # A: count number of nonegative integers
    positives = 0
    for elem in arr:
        if elem > 0:
            positives += 1
    # B: if it's less than 2
    if positives < 2:
        # return the maximum
        return max(arr)
    # C: otherwise compute sums
    # Ca: compute the sum of every even numbered element
    max_sum_even = compute_sum()
    # Cb: compute the sum of every odd numbered element
    max_sum_odd = compute_sum(even=False)
    # Cc: compare sums to see if odd sum is greater than the even
    if max_sum_odd > max_sum_even:
        return max_sum_odd
    # Cd: return the higher of the two
    return max_sum_even


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + "\n")

    fptr.close()
