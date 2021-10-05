import math


def root(x, n):
    """
    find the positvie root

    input:  x = 7, n = 3
    output: 1.913
            6      1
        1        7   8
    <------------------->
        1            2

    1.842

        diff of lower_bound + ( 1- 1/6) = 1.84
                            1.913


    decision space
    l                  higher
    [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
        [1.91, ... 2.]
                        1.5^3 < x = 7
                        1.8^3 < x =7
                        1.9^3 < x = 7

            3^2 = 9

    input:  x = 9, n = 2
    output: 3

    9
    n = 2
        4     9      16
    <------------------->
        2            4

            3^2 = 9

    # approach:

    - find out the lower and higher bound for the x (perfect nums)
        - find a h_bound ^ n > x,
        1,
        - l_bound = h_bound - 1
    - guess and check l_bound and h_bound are answer
    - binary search:

    O(x)
    O(log(decision_space))

    """
    # Early exit:
    if x == 0 or x == 1:
        return x
    # init the lower and upper bounds
    lower = 0
    upper = max(1, x)
    # init the approximate root, by taking the average
    root = (upper + lower) / 2
    # binary search the decision space (what's between the bounds)
    while (root - lower) >= 0.001:
        # bring down the upper bound
        if math.pow(root, n) > x:
            upper = root
        # bring up the lower bound
        elif math.pow(root, n) < x:
            lower = root
        # root has been found
        else:  # math.pow(root, n) == x
            return root
        # otherwise, recalculate the next value to try for the root
        root = (upper + lower) / 2

    """
    def binary_search(low_idx, high_idx, array=None):
        # middle value
        middle = (low_idx + high_idx) // 2
        # middle = array[mid_idx]
        if math.pow(middle, n) == x:
            return middle
        elif math.pow(middle, n) < x:
            return binary_search(middle + 0.001, high_idx)
        elif math.pow(middle, n) > x:
            return binary_search(low_idx, middle - 0.001)

    # A: find the higher bound
    higher = 0
    while math.pow(higher, n)  < x:
        higher += 1
    # B: find the lower bound
    lower = higher - 1
    # C: binary search
    binary_search(lower, higher)
    """
    """
    possible_root = lower
    while math.pow(possible_root, n) < x:
        possible_root += 0.001
    return possible_root
    """
    """
    possible_roots = [
        root in range(lower, higher + 1, 0.001)
    ]
    low, high = 0, len(possible_roots) - 1
    return binary_search(low, high, possible_roots)
    """
