def moveZerosToEnd(arr):
    """Moving zeros to the end using 2 pointers"""
    # set a pointer at the first 0 elem in the array
    zero = 0
    # find the first 0 in the array
    while zero < len(arr) and arr[zero] != 0:
        zero += 1
    # init a pointer for the next element (might be nonzero)
    nonzero = zero + 1
    # move zeros to the back
    while zero < len(arr) and nonzero < len(arr):
        # no need to swap 0's with each other - just move nz right
        if arr[nonzero] == 0:
            nonzero += 1
        # use the pointers to swap
        else:
            arr[zero], arr[nonzero] = arr[nonzero], arr[zero]
            # then move forward in the array
            zero += 1
            nonzero += 1
    return arr

    # time is linear, space is constant

    """
                                  z           nz z
  arr = [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
  
  z  = 5
  nz  = 8
  """
