#!python
import sys


# Helper functions
def clean_scores(scores):
    '''Filters the scores list to obtain all numerical values.'''
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
       5. Input is immutable.

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
       5. Input is immutable.

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


def find_minimum_index(high_scores):
    '''Returns the index of the lowest value in a list of numbers.'''
    # uses linear search
    min_index, minimum = 0, high_scores[0]
    for i in range(len(high_scores)):
        score = high_scores[i]
        if score < minimum:
            minimum = score
            min_index = i
    return min_index


def personal_top_three(scores):
    """Returns a sublist of the three highest scores, arranged in order from
       greatest to least.

       Assumptions:
       1. scores is an unsorted list of only numerical values.
       2. scores may contain duplicates, positive and negative values, and
          integer as well as float values.
       3. The input is immutable.
       4. There may not always be 3 top scores to return.

    """
    # clean the list of numerical values
    candidate_scores = clean_scores(scores)
    # if there's not more than 3 scores, return whatever is in the list
    if len(candidate_scores) <= 3:
        return sorted(candidate_scores, reverse=True)
    # load first 3 into a sublist
    highest = candidate_scores[:3]
    # keep track of the minimum in the highest
    min_index = find_minimum_index(highest)
    # traverse through rest of scores to see if they belong in the top 3
    for score_position in range(3, len(scores)):
        next_score = candidate_scores[score_position]
        # if this next score belongs in the top 3
        if next_score > highest[min_index]:
            # then put in place of current minimum of the top 3
            highest[min_index] = next_score
            # recalculate the index of the min in top 3 scores
            min_index = find_minimum_index(highest)
    # sort the top 3 in descending order (aka the reverse of ascending order)
    return sorted(highest, reverse=True)


if __name__ == '__main__':
    # Good inputs
    scores = [4, 5, 6, -9, 11]
    assert personal_best(scores) == 11
    assert latest(scores) == 11
    assert personal_top_three(scores) == [11, 6, 5]

    scores = [2.3, 2, -5]
    assert personal_best(scores) == 2.3
    assert latest(scores) == -5
    assert personal_top_three(scores) == [2.3, 2, -5]

    # Bad Inputs
    scores = [2.3, 2.0, 'birthday party']
    assert personal_best(scores) == 2.3
    assert latest(scores) == 2.0
    assert personal_top_three(scores) == [2.3, 2]

    scores = ['birthday party']
    assert personal_best(scores) == "Top score is unavailable right now."
    assert latest(scores) == "Scores are unavailable right now."
    assert personal_top_three(scores) == []

    # Edge Cases
    scores = []
    assert personal_best(scores) == "Top score is unavailable right now."
    assert latest(scores) == "Scores are unavailable right now."
    assert personal_top_three(scores) == []

    scores = [5, 5, 5, 5]
    assert personal_best(scores) == 5
    assert latest(scores) == 5
    assert personal_top_three(scores) == [5, 5, 5]

    # Success Message
    print('Hooray! All the test inputs were processed successfully!')
