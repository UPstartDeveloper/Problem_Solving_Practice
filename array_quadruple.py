def find_array_quadruplet_naive(arr, s):
    '''Returns a quadtuple of elements in arr, that sum to s, in sorted order.'''
    solution = []
    arr.sort()  # n log n
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                for k in range(len(arr)):
                    if k != j and k != i:
                        for l in range(len(arr)):
                            if l != i and l != k and l != j:
                                p1, p2, p3, p4 = (arr[i], arr[j], arr[k], arr[l])
                            if (p1 + p2 + p3 + p4) == s:
                                return sorted([p1, p2, p3, p4])
    return solution 

def find_array_quadruplet_quadratic(arr, s):
    # how do I find the two sum? --> two pointers
    # how do I find the three sum? two pointers + index
    # how do I find the four sum? two pointers and two indices
    arr.sort()
    # save a reference to the first index
    index_first_addend = 0
    print(arr)
    while index_first_addend < len(arr) - 3:
        # get the element at that index
        first_addend = arr[index_first_addend]
        # init the second index
        index_second_addend = index_first_addend + 1
        # traverse the rest of the array
        while index_second_addend < len(arr) - 2:
            # save the value of the second addend
            second_addend = arr[index_second_addend]
            # save the index and value of the third addend
            index_third_addend = index_second_addend + 1
            # find the sum left to make
            two_sum = s - (first_addend + second_addend)
            # iterate over all possible quadruplets with the remaining numbers
            index_fourth_addend = len(arr) - 1
            while index_fourth_addend > index_third_addend:
                # get the third and fourth addend
                third_addend = arr[index_third_addend]
                fourth_addend = arr[index_fourth_addend]
                # try adding the four addends together
                summation = (
                    first_addend + second_addend + third_addend + fourth_addend
                )
                if summation == s:
                    return [
                        first_addend,
                        second_addend,
                        third_addend,
                        fourth_addend
                    ]
                elif summation > s:
                    index_fourth_addend -= 1
                elif summation < s:
                    index_third_addend += 1
            # move ahead the second index
            index_second_addend += 1 
        # iterate to the next possible index to find a solution
        index_first_addend += 1
    return list()


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 7, 9]
    target = 20
    print(find_array_quadruplet_quadratic(nums, target))
