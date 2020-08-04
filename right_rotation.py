def rotate_array(input_array, k):
    '''Perform k right rotations on input_array, in O(1) memory.'''
    for _ in range(k):
        # index the element from right
        last = input_array[-1]
        # copy element from front into a temporary variable
        first = input_array[0]
        # move the last element into the first index
        input_array[0] = last
        # shift all other elements to the right
        for index in range(1, len(input_array)):
            # use another temp variable for the value currently in array
            temp = input_array[index]
            input_array[index] = first
            first = temp