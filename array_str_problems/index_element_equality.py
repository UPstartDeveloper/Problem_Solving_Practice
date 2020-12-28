def index_equals_value_search(arr):
    """
    input: arr = [-8,0,2,5]
    output: 2 # since arr[2] == 2
    
    Intuition:
    linear search for all elems i  == arr[i]
    
    Approach:
    store the elems in another array
    [2]
    return the min, or -1
    """
    
    # I don't think I can hear you anymore
    # Did my idea make sense? nope
    # can you hear me now ?
    # this approach looks fine, but can you think of more efficient one.
    # Also, does your solution uses all provided information?
    # i can hear you
    """
    I see, so the arr is sorted
    
    Binary Search - find an elem in log(n)
    
    0       3
    [-8,0,2,5]
            ^
            3
    [-1,0,3,6]
            ^
            
    [0 4 5 8 9]    
            2  3
    [-6, 7, 2, 4, 6, 7]
    
    random index: 3
    0 1 2 3 4
    # if arr[index] >= index --> go to left, and if == save the answer
    # if arr[index] < index --> right side
    # if arr[index] == index --> potential answer, go to left
    
    binary - loop low >= high
    """
    # init low and high
    low, high = 0, len(arr) - 1
    # answer starts -1
    answer = -1
    # loop using binary search
    while low <= high:
        # init the middle
        middle = (low + high) // 2
        mid_elem = arr[middle]
        # answer found
        found = False
        if mid_elem == middle:
            found = True
            answer = mid_elem
        # deal with off-by-one cases
        elif abs(middle - mid_elem) == 1:
            if middle < len(arr) - 1 and arr[middle + 1] == mid_elem:
                found = True
                answer = mid_elem
            elif 0 < middle and arr[middle - 1] == mid_elem:
                found = True
                answer = mid_elem
        if found is True:
            high = middle - 1
        # continue w/ binary search
        else:
            if mid_elem > middle:
                high = middle - 1
            elif mid_elem < middle:
                low = middle + 1

        """                                               0  1  2  3  4  5
        l       m       h       f       a       me       [1, 1, 4, 8, 8, 9]
        0       2       5       F       -1      4
                0       1                       1
                        -1


        # if arr[index] >= index --> go to left, and if == save the answer
        if mid_elem >= middle:
            # save the answer
            if mid_elem == middle or (middle >= 1 and arr[middle - 1] == mid_elem):
                answer = middle
            # go to left,
            high = middle - 1
        # if arr[index] < index --> right side
        elif mid_elem < middle:
            if (middle < len(arr) - 1 and arr[middle + 1] == mid_elem):
                answer = middle
            low = middle + 1
        """ 

    # return the answer
    return answer


if __name__ == "__main__":
    arr = [4, 1, 1, 8, 8, 9]
    print(index_equals_value_search(arr))
"""   
        0 1 2 3
arr = [-8,0,2,5]

l     h      a      m_idx      m_elem,
0     3      -1     1             0
2    1      2       2            2

O(log(n))
Space: O(1)
"""
