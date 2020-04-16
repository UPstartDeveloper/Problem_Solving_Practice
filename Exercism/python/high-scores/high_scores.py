#!python
import sys


def latest(scores):
    pass


def personal_best(scores):
    """Executes linear search for top score, and returns the value.

       Assumptions:
       scores is an unsorted list of numbers, ints or floating point,
       both positives and negatives, and there may be duplicates.

       Only one score will be returned by this function.

       Problem was provided by Exercism:
       https://exercism.io/my/solutions/b50ca3f9f3d54e4fa958ff970aea2489

    """
    # init arbitrarily low value - equals -9223372036854775807, or 2**31-1
    max = -(sys.maxsize - 1)
    for score in scores:
        if score > max:
            max = score
    return max


def personal_top_three(scores):
    pass


if __name__ == '__main__':
    # Good inputs
    scores = [4, 5, 6, -9, 11]
    assert personal_best(scores) == 11

    scores = [2, 2.3, -5]
    assert personal_best(scores) == 2.3
    # Bad Inputs

    # Edge Cases
