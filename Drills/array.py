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
    return None


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


if __name__ == "__main__":
    array = [-7, 2, 1, 6, 7, -90, 5]
    print(merge_sort(array))
