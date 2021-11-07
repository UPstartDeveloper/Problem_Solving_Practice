def majorityElement(nums):
    """Boyer-Moore Voting Algorithm, implemented with assumption all numbers
    in the nums arrays are non-negative.

    :type nums: List[int]
    :rtype: int

    """
    # initialize the canidate for a majority value to a null value
    canidate = -1
    # initialize its count to zero
    count = 0
    # iterate over the nums array
    for index, element in enumerate(nums):
        # set the canidate if needed
        if count == 0:
            canidate = element
        # increment/decrement the count
        if canidate == element:
            count += 1
        else:  # canidate is not the element at this index
            count -= 1
    # return the majority element
    return canidate
