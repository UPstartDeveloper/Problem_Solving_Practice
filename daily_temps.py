def dailyTemperatures(dailyTemps):
    """
    Idea #1: iterative solution

    init an empty list

    iterate over the input list
        iterate until you find an index with greater element,
        or go outside the list
        calculate the difference
        appedn the difference (or 0) to output list

    Complexity Analysis:
    Time - O(n^2) - for each of n iterations, we require an average of
    n/2 iterations to the end of the list. Therefore, the runtime rises asymptotically
    as quadratic function with respect to n, the length of dailyTemps.

    Space - O(n), because the output list is just as long as input

    """
    # useful constant for speed
    NUM_DAYS = len(dailyTemps)  # O(n)
    # init an empty list
    wait_days = list()  # O(1)
    # iterate over input list
    for temp_index, temp_val in enumerate(dailyTemps):  # n iterations
        # find the index of a hotter day, if possible
        next_index = temp_index + 1  # O(1)
        while next_index < NUM_DAYS:  # up to n iterations
            # determine if the temperature on this day is greater
            next_day_temp = dailyTemps[next_index]
            if next_day_temp > temp_val:
                break
            else:  # next_day_temp <= temp_val
                next_index += 1
        # determine the difference between two indices
        difference = next_index - temp_index
        # add difference to the output, if valid
        if difference < NUM_DAYS - temp_index:
            wait_days.append(difference)
        # no hotter day available
        else:
            wait_days.append(0)
    return wait_days


sampleInput = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(sampleInput))


"""
 0.  1.   2.  3.  4.  5.  6.  7  8
[73, 74, 75, 71, 69, 72, 76, 73]

wait_days
[1, ]

NUM_DAYS. | temp_index | temp_val. |  next_day_temp   | diff
  7           1           74            1, 74           1
  
Complexity
"""
