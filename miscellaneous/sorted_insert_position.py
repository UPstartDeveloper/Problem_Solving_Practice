import math


def find_index(sorted_list, target):
    """Finds the index where the target value is expected in a sorted list."""

    def binary_search(low_index, hi_index):
        """Searches for a value in a list, throwing away half each call"""
        # locate the middle index
        mid_index = math.ceil((low_index + hi_index) / 2)
        # obtain values from all three indices
        low_val, mid_val, high_val = (
            sorted_list[low_index],
            sorted_list[mid_index],
            sorted_list[hi_index],
        )
        # Base case: the target value is found
        if mid_val == target:
            return mid_index
        # target value not found:
        elif mid_val > target:
            # if target lies "before" the array
            if low_index == hi_index:
                # return the 0 index
                return mid_index
            # otherwise search the lower half of the array
            return binary_search(low_index, mid_index - 1)
        elif mid_val < target:
            # if target lies "after" the last value
            if low_index == hi_index:
                return mid_index + 1
            # otherwise search the larger half of the array
            return binary_search(mid_index + 1, hi_index)

    # store the array length
    ARRAY_LENGTH = len(sorted_list)
    # execute binary search on the array
    return binary_search(0, ARRAY_LENGTH - 1)


if __name__ == "__main__":
    print(find_index([1, 3, 5, 6], 5))
