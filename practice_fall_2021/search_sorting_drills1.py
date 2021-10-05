from typing import List


class Array:
    def __init__(self, items: List[int]) -> None:
        self.list = items

    def search(self, target: int, linear=True, use_iteration=True):
        """Return -1 if the integer is not found"""

        def _search_linear_iter():
            for ndx in range(len(self.list)):
                item = self.list[ndx]
                if item == target:
                    return ndx
            return -1

        def _search_linear_recursive(index=0):
            if index < len(self.list):
                # base: found
                if self.list[index] == target:
                    return index
                # recursive case
                return _search_linear_recursive(index + 1)
            # base: not found
            return -1

        def _search_binary_iter():
            # start w/ whole array
            low, high = 0, len(self.list) - 1
            # divide and conquer
            while low <= high:
                # find middle
                mid = (low + high) // 2
                mid_elem = self.list[mid]
                # found
                if target == mid_elem:
                    return mid
                # to the next subproblem
                elif target < mid_elem:
                    high = mid - 1
                else:  # target value is to the right
                    low = mid + 1
            # not found
            return -1

        def _search_binary_recursive(low=0, high=None):
            """
            Test Cases(array, target):
            [], -3
            [-3], -3
            [-5], -3


            """
            # start w/ whole array
            if high is None:
                high = len(self.list) - 1
            # not found
            elif low > high:
                return -1
            # find the middle
            mid_ndx = (low + high) // 2
            mid = self.list[mid_ndx]
            # found
            if target == mid:
                return mid_ndx
            # divide (and then conquer)
            elif target < mid:  # move left
                return _search_binary_recursive(low, mid - 1)
            else:  # move right
                return _search_binary_recursive(mid + 1, high)

        if linear is True:
            if use_iteration:
                return _search_linear_iter()
            return _search_linear_recursive()
        else:  # using binary search
            if use_iteration:
                return _search_binary_iter()
            return _search_binary_recursive()

    """TODO"""

    def sort_recursively(self, inplace=True):
        def _quick_sort():
            pass

        def _merge_sort():
            pass

        if inplace:
            return _quick_sort()  # not stable
        return _merge_sort()  # not mutative

    def bubble_sort(self):
        """mutative"""
        pass

    def insertion_sort(self):
        """mutative"""
        pass
