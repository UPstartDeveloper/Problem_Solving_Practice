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

       I am not allowed to mutate the input.

       Problem was provided by Exercism:
       https://exercism.io/my/solutions/b50ca3f9f3d54e4fa958ff970aea2489

    """
    # take all unique numerical values into a separate list
    scores_set = list()
    for score in scores:
        if (isinstance(score, int) or isinstance(score, float)):
            scores_set.append(score)
    # if there were no numrical scores, exit function
    if len(scores_set) == 0:
        return "Top score is unavailable right now."
    # loop through the set of candidate scores
    max = scores_set[0]
    for i in range(len(scores_set)):
        score = scores_set[i]
        # if the score is the largest we've seen so far, it's the maximum
        if score > max:
            max = score
    # return the max score
    return max


def personal_top_three(scores):
    pass


if __name__ == '__main__':
    # personal_best function
    # Good inputs
    scores = [4, 5, 6, -9, 11]
    assert personal_best(scores) == 11

    scores = [2.3, 2.0, -5]
    assert personal_best(scores) == 2.3, f'Returned: {personal_best(scores)}'
    # Bad Inputs
    scores = [2.3, 2.0, 'birthday party']
    assert personal_best(scores) == 2.3

    scores = ['birthday party']
    assert personal_best(scores) == "Top score is unavailable right now."

    # Edge Cases
    scores = []
    assert personal_best(scores) == "Top score is unavailable right now."

    scores = [5, 5, 5, 5]
    assert personal_best(scores) == 5
