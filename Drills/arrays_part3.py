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
        # insert the elements after the first
        for index in range(1, len(self.arr)):
            # insert this next element
            element = self.arr[index]
            while index > 0:
                prev_index = index - 1
                prev_elem = self.arr[prev_index]
                # make swaps as needed
                if prev_elem > element:
                    self.arr[prev_index] = element
                    self.arr[index] = prev_elem
                index -= 1

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
                elem, elem_after = (self.arr[index], self.arr[index_after])
                # swap
                if elem_after < elem:
                    self.arr[index] = elem_after
                    self.arr[index_after] = elem
                    swaps += 1
                # move on to next element
                index += 1

    def mergesort(self, array):
        def merge(left, right):
            # init new array
            merged = list()
            # battle for the spots in the new array
            ndx_l, ndx_r = 0, 0
            while ndx_l < len(left) and ndx_r < len(right):
                elem_l, elem_r = left[ndx_l], right[ndx_r]
                # decide the element to go next
                if elem_l <= elem_r:
                    merged.append(elem_l)
                    ndx_l += 1
                else:
                    merged.append(elem_r)
                    ndx_r += 1
            # add any remaining items
            if ndx_l < len(left):
                for elem_l in left[ndx_l]:
                    merged.append(elem_l)
            if ndx_r < len(right):
                for elem_r in right[ndx_r]:
                    merged.append(elem_r)
            # return new array
            return merged

        # Base Case
        if len(array) >= 2:
            # Divide - find the middle of the list
            mid = len(self.arr) // 2
            # Conquer - sort the halves of the list
            sorted_left = self.mergesort(array[:mid])
            sorted_right = self.mergesort(array[mid:])
            # Combine - merge the sorted halves
            array = merge(sorted_left, sorted_right)
        return array

    def quicksort(self, inplace=True):
        def _quick_sort_internal(low=0, high=None):
            """
            This implementation of Quicksort has the following attrs:
            - Time: O(n log n) - avg case, which depends on if
                    the last element (which we choose as
                    the pivot) is near the median of
                    the subarray we are sorting

                  O(n^2) --> if the pivot is near the min or max
                             of the subarrays we sort

            - Space: O(log n) for the amount of space needed for the
                             call stack, given the # of stack frames
                             we push
                   O(n) in the worst case, as the subarrays get smaller

            - Internal --> b/c we mutate the array in place

            - Recurisively implemented, not just iterative

            - UNSTABLE algorithm

            - This IS a comparision sorting algorithm

            - Mistakes while implementing:
                1) make sure to recursively call the Quicksort func,
                    - the partition() should be called once per stack frame,
                      because we need it to happen as a subroutine
                      - i.e. it's great that it divides the array for us,
                            it's just that it's only once we have quicksort
                            algo recurse do we actually sort the array fully
                            (b/c it's the larger QS func that actually decides
                            if we need to continue sorting after partitioning)
            """

            def partition(low, high) -> int:
                """
                returns the pivot index after the element
                at the end of this subarray
                defined by low and high is sorted
                """
                # choose the last element in the subarray as pivot
                pivot = self.arr[high]
                # swap elements less than the pivot into place
                lower_side_tail, swapper = low - 1, low
                while swapper < high:
                    # throwing the smaller elements "behind" the swapper
                    if self.arr[swapper] < pivot:
                        lower_side_tail += 1
                        self.arr[lower_side_tail], self.arr[swapper] = (
                            self.arr[swapper],
                            self.arr[lower_side_tail],
                        )
                    # continue sorting the subarray
                    swapper += 1
                # move the pivot element into its sorted position
                self.arr[lower_side_tail + 1], self.arr[high] = (
                    pivot,
                    self.arr[lower_side_tail + 1],
                )
                # return the new position of the pivot
                return lower_side_tail + 1

            ############### Driver Code ###############################

            # init the high index as needed
            if high is None:
                high = len(self.arr) - 1
            # Divide: partition the subarray around the pivot
            pivot = partition(low, high)
            # Conquer: recurse on the subarrays to left and right of the pivot
            if pivot - low > 1:
                _quick_sort_internal(low, pivot - 1)
            if high - pivot > 1:
                _quick_sort_internal(pivot + 1, high)

        def _quick_sort_external():
            pass

        if inplace is True:
            return _quick_sort_internal()
        return _quick_sort_external()


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
    # array.arr = items
    # array.sort_bubble()
    # assert sorted(items) == array.arr

    ## Bubble Sort
    array.arr = items
    print(f"Items before sorting: {items}")
    array.quicksort()
    print(f"Items before sorting: {array.arr}")
    assert sorted(items) == array.arr
