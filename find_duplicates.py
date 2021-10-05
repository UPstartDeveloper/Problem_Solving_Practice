def find_duplicates(arr1, arr2):
    """
    differing sizes
    >= ints
    sorted
    unique ints in each arr


    arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

    # Brute force -
    - iterative
    - quadratic

    # Idea - Sets

    {1, 2, 3, 5, 6, 7}
    [3]

    {3, 6, 7} = [3, 6, 7]

    S = smaller arraty
    L = larger


    Space = L
    Time = S + L

    Idea - Searching

    find smaller array - constant
    iterate over the smaller one - S iterations
        binary search for it in the larger one - log L
        if so, add to the intersections

    Time: O(S log L)
    Space: O(S)
    ----------------------
    constant space
    linear time

    same length

    sesarch

    arr1 = [1, 2, 3, 5, 6, 7],
    arr2 = [3, 6, 7, 8, 20, 34]
    ans = [3]

                    v
    arr1 = [1, 2, 3, 8, 10, 11],
                v
    arr2 = [3, 6, 7, 8, 20, 34]



    <---- 1 -3---------- 7 -->
            3-------------------------34
    """
    # find smaller array - constant
    smaller = None
    larger = None
    if len(arr1) <= len(arr2):
        smaller = arr1
        larger = arr2
    else:
        smaller = arr2
        larger = arr1
    answer = list()
    # init two pointers in both arrays
    ps = 0
    pl = 0

    while ps < len(smaller) and pl < len(larger):
        # compare
        if smaller[ps] == larger[pl]:
            answer.append(smaller[ps])
            ps += 1
            pl += 1
        elif smaller[ps] > larger[pl]:
            pl += 1
        else:
            ps += 1
    return answer

    """
    def binary_search(target, lo, hi, array):
        # calculate the middle index and element
        mid = (lo + hi) // 2
        middle_elem = array[mid]
        # compare it to the target 
        if target == middle_elem:
        # ==, return index
        return mid
        # !=, last index --> -1
        elif lo >= hi:
        return -1
        # >, search the lower half
        elif target > middle_elem:
        return binary_search(target, mid + 1, hi, array)
        # <, search the greater half
        else:  # target > middle_elem
        return binary_search(target, lo, mid - 1, array)
    # find smaller array - constant
    smaller = None
    larger = None
    if len(arr1) <= len(arr2):
        smaller = arr1
        larger = arr2
    else:
        smaller = arr2
        larger = arr1
    # iterate over the smaller one - S iterations
    answer = list()
    for elem in smaller:
        # binary search for it in the larger one - log L
        larger_index = binary_search(elem, 0, len(larger) - 1, larger)
        # if so, add to the intersections
        if larger_index > -1:
        answer.append(elem)
    return answer
    """

    """
    Test Case 1
                0. 1. 2. 3. 4. 5 
    l = arr1 = [1, 2, 3, 5, 6, 7], 
                            l  h
                            m
    s = arr2 = [3, 6, 7, 8, 20]

    ans = [3, 6, 7]

    elem = 3
    """
