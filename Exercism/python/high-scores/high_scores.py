#!python
import sys


# Helper functions
def clean_scores(scores):
    '''Filters the scores list of non-numerical values.'''
    candidate_scores = list()
    for score in scores:
        if (isinstance(score, int) or isinstance(score, float)):
            candidate_scores.append(score)
    return candidate_scores


# Solutions
def latest(scores):
    """Return the value that was added last to a list of scores.
       Assumptions:
       1. scores is a list.
       2. All numerical values present are sorted in order of date added, from
          earliest to latest.
       3. There may be other data types present, yet only ints and floats are
          valid return types.
       4. Numerical values may have duplicates, and they may contain a mixture
          of positive or negative numbers, or integer and floating point
          numbers.

       I am not allowed to mutate the input.

       Problem was provided by Exercism:
       https://exercism.io/my/solutions/b50ca3f9f3d54e4fa958ff970aea2489
    """
    # take all unique numerical values into a separate list
    candidate_scores = clean_scores(scores)
    # if there were no numrical scores, exit function
    if len(candidate_scores) == 0:
        return "Scores are unavailable right now."
    # if there are one or more numbers left, return the last
    return candidate_scores[-1]


def personal_best(scores):
    """Executes linear search for top score, and returns the value.

       Assumptions:
       1. scores is an unsorted list.
       2. There may be duplicates.
       3. Other data types may also appear, and only floats and ints are valid
          as return values.
       4. Only one score can be returned by this function.
       5. I am not allowed to mutate the input.

       Problem was provided by Exercism:
       https://exercism.io/my/solutions/b50ca3f9f3d54e4fa958ff970aea2489

    """
    # take all unique numerical values into a separate list
    candidate_scores = clean_scores(scores)
    # if there were no numerical scores, exit function
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
