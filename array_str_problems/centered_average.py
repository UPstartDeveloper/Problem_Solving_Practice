def centered_average(nums):
    """
    take out 1 value of the smallest and largst
    compute and return the mean of the rest
    int div --> truncate the floating part?


    ASSUME:
    +3 ints
    pos/neg
    unsorted
    dupes possible

    Intutition:
      - computing an average (sum / # of points)

    Approach:
    1. Simple
      - compute the min
      - compute the max
      - sum the whole list
      - subtract (min), and subtract max
      - return (remaining_sum) by (len = 2)

    Edge Cases:
    - all negatives --> normal
    - if in prod and saw input that broke constraints --> Error
    """
    # - compute the min
    # - compute the max
    min_val, max_val = min(nums), max(nums)
    # - sum the whole list
    total = sum(nums)
    # - subtract (min), and subtract max
    remaining_sum = total - (min_val + max_val)
    # - return (remaining_sum) by (len = 2)
    return int(remaining_sum / (len(nums) - 2))
