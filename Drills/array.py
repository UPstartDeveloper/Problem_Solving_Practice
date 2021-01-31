"""

Common Array Methods Needed:

1. Binary Search

2. Sorting
- Merge Sort
- QuickSort
- Bucket Sort
- Insertion Sort

"""


def binary_search(array, x):
    """
    Vanilla BS algorithm
    Look for x in the sorted array
    return the index if found
    or else return None


    [8, 9, 10]
    """
    # A: init the low and high values
    low, high = 0, len(array) - 1
    # B: search the array
    while low <= high:
        # find the middle value
        middle  = (low + high) // 2
        mid_elem = array[middle]
        # if found, return the index
        if mid_elem == x:
            return middle
        # if not, divide the array into two subproblems 
        elif mid_elem < x:  # go right
            low = middle + 1
        elif mid_elem > x:  # go left
            high = middle - 1
    # C: if not found, return None
    return -1


def binary_search_recursive(array, target, low=None, high=None):
    if low is None:
        low, high = 0, len(array) - 1
    mid_idx = (low + high) // 2
    middle = array[mid_idx]
    # Base Case:
    # target found
    if middle == target:
        return mid_idx
    # target not in array
    elif low > high:
        return -1
    # Recurisive Cases:
    # middle is <  target
    elif middle < target:
        return binary_search_recursive(mid_idx + 1, high)
    # middle is > target
    else:
        return binary_search_recursive(low, mid_idx - 1)


def merge_sort(array):
    """
    the merge sort algorithm sorts an array of elements 
    out of place, is stable, and takes O(n log n) time

    Divide: split the array into left and right halves
    Conquer: sort the half
    Combine: merge the two sorted array
    """
    def merge(left, right):
        """Merge two sorted lists into a combined sorted list"""
        # A: init the new array
        combined = list()
        # B: have the two array "battle" for each position in the combined 
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            # get the next elements from both
            left_elem = left[left_idx]
            right_elem = right[right_idx]
            # lowest value gets the spot (left gets priority, so it's stable)
            if left_elem <= right_elem:
                combined.append(left_elem)
                left_idx += 1
            else:  # left_elem > right_elem
                combined.append(right_elem)
                right_idx += 1
        # C: also insert any leftovers at the end 
        if left_idx < len(left):
            combined.extend(left[left_idx:])
        elif right_idx < len(right):
            combined.extend(right[right_idx:])
        return combined

    # Base Case: if the array has one (or zero elements?), it's sorted
    # Recursive: more than 1 element
    if len(array) > 1:
        # find the middle
        middle = len(array) // 2
        # sort the left
        sorted_left = merge_sort(array[:middle])
        # sort the right
        sorted_right = merge_sort(array[middle:])
        # merge the two
        array = merge(sorted_left, sorted_right)
    # return the sorted array
    return array


def quick_sort(array, low=0, high=None):
    """
    Divide and conquer sorting algorithm
    that is in place and not stable.
    O(n log n) time and O(log n) space in 
    the average case
    """
    def partition(low, high):
        # the first element will be the pivot
        pivot = low
        # swap elements left and right, based on pivot's value
        left = pivot + 1
        right = high
        while right > left:
            # find an element > pivot
            while left < len(array) - 1 and array[left] < array[pivot]:
                left += 1
            # find an element < pivot
            while right > 0 and array[right] > array[pivot]:
                right -= 1
            # swap
            if left < len(array) - 1 and right > 0:
                array[left], array[right] = array[right], array[left]
                # print(f"Just swapped", array)
                # left, right = right, left
                break
            # print(f"Left is {left} and right is {right}" )
        # move pivot into the sorted position
        if left < len(array) and right > 0:
            array[pivot], array[left] = array[left], array[pivot]
        # return the new location of the pivot
        # print(f"Returning {left}, array is {array}")
        return left
    # init the subrange over the whole array
    if high is None:
        high = len(array) - 1
    # base case case: zero or 1 elements:
    if high - low < 2:
        return array
    # divide & conquer: partition elements around the pivot
    pivot = partition(low, high)
    print(f"pivot is now {pivot}")
    # continue: partition both sides of the (sorted) pivot
    quick_sort(array, low, pivot - 1)
    quick_sort(array, pivot, high)
    return array


def insertion_sort(array):
    """
    Intuition: 
    - let's mark the first index in the array as sorted
    - then iteratively add more and more elements into their sorted
        position, in the sorted section
    Approach:
    # - for every elem after index 0
    #     - loop backwards through the sorted section
    #         - if the number before is greater, swap (stop at index 0)
    #         - if the number before is less/equal, stop early

    [5, 6, -2, 6, 2, 1, 7]
    [5, -2, 6, 6, 2, 1, 7]
    [-2, 5, 6, 6, 2, 1, 7]

    Assumption
    Edge Cases:
    - array of length <= 1 --> return array
    - not an array --> ValueError
    - we don't have all of the same data type in the array --> ValueError
    """

    def is_consistent(array) -> bool:
        # TODO: linear pass to ensure all the elements have same data type
        index = 0

        while index < len(array) - 1:
            elem, elem_ahead = array[index], array[index + 1]
            if type(elem) != type(elem_ahead):
                return False
            index += 1
        return True

    if not isinstance(array, list) or not is_consistent(array):
        raise ValueError(
            "This array must contain 1 or more elements of the same data type"
        )
    elif len(array) > 0:
        # for every elem after index 0
        for index in range(1, len(array)):
            index_before = index - 1
            # if the number before is greater, swap (stop at index 0)
            while index_before > -1 and array[index_before] > array[index]:
                array[index], array[index_before] = (
                    array[index_before], array[index]
                )
                index -= 1
                index_before -= 1
    return array

"""
 0  1   2  3  4  5  6
[5, 6, -2, 6, 2, 1, 7]
[5, -2, 6, 6, 2, 1, 7]
[-2, 5, 6, 6, 2, 1, 7]

i       ib
1       0  
2       1 
1       0  
0       -1
3       2
4       3
"""

if __name__ == "__main__":
    array1 = [-7, 2, 1, 6, 7, -90, 5]
    array2 = [4, 2, 3, 9, 5, 2]
    # print(merge_sort(array2))
    print(quick_sort(array1))
    print(quick_sort(array2))
    # print(insertion_sort([5, 6, -2, 6, 2, 1, 7]))
