"""
Problem Statement:

Given a non-empty array of integers,
every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

"""


def single_number(integers):
    unique = 0
    for integer in integers:
        unique ^= integer
        # print(unique)
    return unique


if __name__ == "__main__":
    assert single_number([-1, 1, 2, 1, 2]) == -1
    # if unique is 0, it either means 0 is the single integer
    assert single_number([0, 1, 2, 1, 2]) == 0
    # or there is no single int at all (and this is considered an edge case)
    assert single_number([1, 2, 1, 2]) == 0
