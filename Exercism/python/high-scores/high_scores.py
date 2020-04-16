#!python
import sys


def latest(scores):
    """Return the value that was added last to a list of scores.
       Assumptions:
       scores is an sorted list of numbers, ints or floating point,
       both positives and negatives, and there may be duplicates, and is
       in order of when the user hit that score (i.e. earliest score is at
       first index).

       I am not allowed to mutate the input.

       Problem was provided by Exercism:
       https://exercism.io/my/solutions/b50ca3f9f3d54e4fa958ff970aea2489
    """
    # take all unique numerical values into a separate list
    candidate_scores = list()
    for score in scores:
        if (isinstance(score, int) or isinstance(score, float)):
            candidate_scores.append(score)
    # if there were no numrical scores, exit function
    if len(candidate_scores) == 0:
        return "Scores are unavailable right now."
    # if there are one or more numbers left, return the last
    return candidate_scores[-1]


def personal_best(scores):
    """Executes linear search for top score, and returns the value.

       Assumptions:
       scores is an unsorted list of numbers, ints or floating point,
       both positives and negatives, and there may be duplicates.

       Only one score can be returned by this function.

       I am not allowed to mutate the input.

       Problem was provided by Exercism:
       https://exercism.io/my/solutions/b50ca3f9f3d54e4fa958ff970aea2489

    """
    # take all unique numerical values into a separate list
    candidate_scores = list()
    for score in scores:
        if (isinstance(score, int) or isinstance(score, float)):
            candidate_scores.append(score)
    # if there were no numrical scores, exit function
    if len(candidate_scores) == 0:
        return "Top score is unavailable right now."
    # loop through the set of candidate scores
    max = candidate_scores[0]
    for i in range(len(candidate_scores)):
        score = candidate_scores[i]
        # if the score is the largest we've seen so far, it's the maximum
        if score > max:
            max = score
    # return the max score
    return max


def personal_top_three(scores):
    pass


if __name__ == '__main__':
    # Good inputs
    scores = [4, 5, 6, -9, 11]
    assert personal_best(scores) == 11
    assert latest(scores) == 11

    scores = [2.3, 2.0, -5]
    assert personal_best(scores) == 2.3, f'Returned: {personal_best(scores)}'
    assert latest(scores) == -5

    # Bad Inputs
    scores = [2.3, 2.0, 'birthday party']
    assert personal_best(scores) == 2.3
    assert latest(scores) == 2.0

    scores = ['birthday party']
    assert personal_best(scores) == "Top score is unavailable right now."
    assert latest(scores) == "Scores are unavailable right now."

    # Edge Cases
    scores = []
    assert personal_best(scores) == "Top score is unavailable right now."
    assert latest(scores) == "Scores are unavailable right now."

    scores = [5, 5, 5, 5]
    assert personal_best(scores) == 5
    assert latest(scores) == 5

    # Success Message
    print('Hooray! All the test inputs were processed successfully!')
