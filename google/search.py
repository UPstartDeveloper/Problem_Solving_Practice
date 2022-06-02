from typing import List


def search(array: List[int], target: int, use_binary=True, use_iter=True) -> int:
    ### HELPERS
    def _linear_recursive(index=0):
        # base cases
        if index == len(array):
            return -1
        elif index < len(array):
            if array[index] == target:
                return index
            # recursive case
            else:
                return _linear_recursive(index + 1)

    def _linear_iterative():
        for index, item in enumerate(array):
            if item == target:
                return index
        return -1

    def _binary_recursive(lo=0, hi=len(array) - 1):
        # base case: not found
        if lo > hi:
            return -1
        # base case: found
        mid = (lo + hi) // 2
        found = array[mid]
        if target == found:
            return mid
        # recursive cases:
        if target < found:
            return _binary_recursive(lo, mid - 1)
        elif target > found:
            return _binary_recursive(mid + 1, hi)

    def _binary_iterative():
        lo, hi = 0, len(array) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            found = array[mid]
            if target == found:
                return mid
            elif target < found:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    ### DRIVERS
    choose_helper = {
        True: [_binary_recursive, _binary_iterative],
        False: [_linear_recursive, _linear_iterative],
    }
    return choose_helper[use_binary][int(use_iter)]()
