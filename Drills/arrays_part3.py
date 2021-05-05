class Array:

    def __init__(self, items):
        self.arr = items

    def search_linear(self, target, use_iter=True):

        def _iterative():
            # for each item, check if target found (exit early)
            for index in range(len(self.arr)):
                item = self.arr[index]
                # found
                if item == target:
                    return index
            # not found
            return -1

        def _recursive(index=0):
            # not found
            if index == len(self.arr):
                return -1
            # found
            elif self.arr[index] == target:
                return index
            # recursive case
            return _recursive(index + 1)
    
        if use_iter is True:
            return _iterative()
        return _recursive()

    def search_binary(self, target, use_iter=True):
        # ASSUME the array is already sorted 
        def _iterative():
            # init low and high
            low, high = 0, len(self.arr) - 1
            # divide and conquer
            while low <= high:
                mid = (low + high) // 2
                mid_elem = self.arr[mid]
                # found
                if mid_elem == target:
                    return mid
                # go left 
                elif mid_elem > target:
                    high = mid - 1
                # go right 
                elif mid_elem < target:
                    low = mid + 1
            # not found
            return -1

        def _recursive(low=0, high=None):
            # init values
            if high is None:
                high = len(self.arr) - 1
            # get middle 
            mid = (low + high) // 2
            mid_elem = self.arr[mid]
            # base - found
            if mid == target:
                return mid
            # base - not found
            elif low > high:
                return -1
            # go left 
            elif mid_elem > target:
                return _recursive(low, mid - 1)
            # go right 
            return _recursive(mid + 1, high)

        if use_iter is True:
            return _iterative()
        return _recursive()

    # Sorting Algorithms

    def sort_insertion(self):
        pass

    def sort_bubble(self):
        # init the number of swaps done on a pass
        swaps = -1
        # swap until sorted
        while swaps != 0:
            # swap any items out of place
            index = 0
            swaps = 0
            while index < len(self.arr) - 1:
                index_after = index + 1
                elem, elem_after = (
                    self.arr[index],
                    self.arr[index_after]
                )
                # swap
                if elem_after < elem:
                    self.arr[index] = elem_after
                    self.arr[index_after] = elem
                    swaps += 1
                # move on to next element
                index += 1


    def mergesort(self):
        pass

    def quicksort(self, inplace=True):
        pass


if __name__ == "__main__":
    # Search Tests
    items = [5, 6, 3, 2, -1, 6, -4]
    array = Array(items)
    ## Linear Search
    assert array.search_linear(6) == 1  # multiple items matching target
    assert array.search_linear(2, False) == 3  # target exists
    assert array.search_linear(7) == -1  # target not found

    ## Binary Search Tests
    array.arr = sorted(items)
    assert array.search_binary(6) == 5  # multiple items matching target
    assert array.search_binary(2, False) == 2  # target exists
    assert array.search_binary(7) == -1  # target not found

    # Sorting Tests
    ## Bubble Sort
    array.arr = items
    array.sort_bubble()
    assert sorted(items) == array.arr
