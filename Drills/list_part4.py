def linear_search(array, target):
    for index in range(len(array)):
        item = array[index]
        if item == target:
            return index
    return -1


def linear_search_recursive(array, target, index=0):
    '''uses recursion'''
    if index == len(array):
        return -1
    elif array[index] == target:
        return index
    else:  # move on the next index
        return linear_search_recursive(array, target, index + 1)


def binary_search_iter(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid_ndx = (low + high) // 2
        mid = array[mid_ndx]

        if mid == target:
            return mid_ndx

        elif mid > target:  # go left
            high = mid_ndx - 1 
        
        elif mid < target:  # go right
            low = mid_ndx + 1
    
    return -1



def binary_search_rec(array, target, low=0, high=None):
    # Base Cases
    if high is None:
        high = len(array) - 1

    if low > high:
        return -1

    mid_ndx = (low + high) // 2
    mid = array[mid_ndx]

    if mid == target:
        return mid_ndx
    # Recursive Cases
    elif mid < target:  # go right
        return binary_search_rec(array, target, mid_ndx + 1, high)
    
    else:  # go left 
        return binary_search_rec(array, target, low, mid_ndx - 1)


def bubble_sort(array):
    '''Sorts the Array in Place'''
    is_sorted = False
    while is_sorted is False:
        swaps = 0
        for index in range(len(array) - 1):
            index_after = index + 1
            elem, elem_after = array[index], array[index_after]
            # swap
            if elem_after < elem:
                array[index], array[index_after] = elem_after, elem
                swaps += 1
        if swaps == 0:
            is_sorted = True
    return array


def insertion_sort(array):
    insert_index = 1
    while insert_index < len(array):
        # make a copy
        index_to_insert = insert_index
        # insrt the element into the right spot
        for index_before in range(insert_index - 1, -1, -1):
            # swap as needed
            elem, elem_before = array[index_to_insert], array[index_before]
            if elem_before > elem:
                array[index_to_insert], array[index_before] = elem_before, elem
                # keep moving back
                index_to_insert -= 1
            # no swap needed - end early [note: can only include this if no duplicates allowed]
            else:
                break
        # move on to the next iteration
        insert_index += 1
    # list is sorted
    return array
    




