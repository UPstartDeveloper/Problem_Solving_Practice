class ArrayList:

    def __init__(self, array):
        self.collection = array

    def search(self, target, is_sorted=False, use_iteration=0):
        """
        functions = {
            True: [BS functions]
            False: [linear search functions]
        }
        """

        def _linear_search_iterative():
            # search items in order of indices
            for index in range(len(self.collection)):
                item = self.collection[index]
                # found
                if item == target:
                    return index
            # not found
            return -1
    
        def _linear_search_recursive(index=0):
            # validate input
            if index < len(self.collection):
                item = self.collection[index]
                # found
                if item == target:
                    return index
                # not found --> recurse
                return _linear_search_recursive(index + 1)
            # not found -> end the search
            return -1

        def _binary_search_iterative():
            # init low and hi
            low = 0
            high = len(self.collection) - 1
            # begin search
            while low <= high:
                # locate the mid
                mid_ndx = (low + high) // 2
                mid_elem = self.collection[mid_ndx]
                # found
                if mid_elem == target:
                    return mid_ndx
                # otherwise, move to the left
                elif mid_elem > target:
                    high = mid_ndx - 1
                # or move to the right
                elif mid_elem < target:
                    low = mid_ndx + 1
            # not found 
            return -1

        def _binary_search_recursive(low=0, high=None):
            # init high
            if high is None:
                high = len(self.collection) - 1
            
            if low <= high:
                # locate the middle
                mid_ndx = (low + high) // 2
                mid_elem = self.collection[mid_ndx]
                # found
                if mid_elem == target:
                    return mid_ndx
                # go left
                elif mid_elem > target:
                    return _binary_search_recursive(low, mid_ndx - 1)
                # go right 
                else: 
                    return _binary_search_recursive(mid_ndx + 1, high)
            # not found
            return -1

        ### DRIVER Code ###

        # choose the search function based on the args
        search_funcs = {
            True: [_binary_search_iterative, _binary_search_recursive],
            False: [_linear_search_iterative, _linear_search_recursive],
        }
        search = search_funcs[is_sorted][use_iteration]
        # search for the target
        return search()

    def bubble_sort(self):
        is_sorted = False
        # begin sorting
        while is_sorted is False:
            swaps = 0
            # start 1 pass through the array
            index = 0
            while index < len(self.collection) - 1:
                index_after = index + 1
                element_before, elem_after = (
                    self.collection[index],
                    self.collection[index_after]
                )
                # swap as needed
                if element_before > elem_after:
                    self.collection[index], self.collection[index_after] = (
                        elem_after, element_before
                    )
                # move on to the next index
                index += 1
            # move on to the next pass as needed
            if swaps == 0:
                 is_sorted = True

    def insertion_sort(self):
        if len(self.collection) > 1:
            # start at the second index
            for index_to_sort in range(1, len(self.collection)):
                # move this element into its sorted position
                while index_to_sort > 0:
                    index_before = index_to_sort - 1
                    element_to_sort, element_before = (
                        self.collection[index_to_sort],
                        self.collection[index_before]
                    )
                    # make a swap
                    if element_before > element_to_sort:
                        self.collection[index_to_sort], self.collection[index_before] = (
                            element_before, element_to_sort
                        )
                        # continue moving backwards
                        index_to_sort -= 1
                    # otherwise move to next iteration
                    else:
                        break

    def merge_sort(self, nums=None):

        def merge(left, right):
            # A: track pos in both halves
            index_left, index_right = 0, 0
            # B: init a third "merged" array
            merged = list()
            # C: have each elem "battle" for the pos in the merged array
            while index_left < len(left) and index_right < len(right):
                elem_l, elem_r = left[index_left], right[index_right]
                if elem_l <= elem_r:  # stable sorting
                    merged.append(elem_l)
                    index_left += 1
                else:
                    merged.append(elem_r)
                    index_right += 1
            # D: add any remaining elements
            pass
            # E: return the merged list
            return merged

        # Base Cases:
        if nums is None:  # need to init the list
            return self.merge_sort(self.collection)
        elif len(nums) < 2:  # already sorted list
            return nums
        # Divide: find the middle index
        mid_ndx = len(nums) // 2
        # Conquer: sort the left side, then the right
        sorted_left = self.merge_sort(nums[:mid_ndx])
        sorted_right = self.merge_sort(nums[mid_ndx:])
        # Combine: merge the sorted halves together
        return merge(sorted_left, sorted_right)

    def quicksort(self, low=0, high=None):
        """TODO: check edge cases"""

        def partition(pivot):
            '''Here, we've chosen the last index as the pivot'''
            lower_side_tail = -1
            swapper = 0
            pivot_val = self.collection[pivot]
            while swapper < pivot:
                # move all the elements encountered < pivot value, backwards
                swapped = self.collection[swapper]
                if swapped < pivot_val:
                    # swap
                    lower_side_tail += 1
                    lst = lower_side_tail
                    # TODO: shorten this line
                    self.collection[swapper], self.collection[lst] = (
                        self.collection[lower_side_tail], swapped 
                    )
                # regardless, move ahead to the next element
                swapper += 1
            # at the end, move the pivot element into place
            self.collection[lower_side_tail + 1], self.collection[pivot] = (
                pivot_val, self.collection[lower_side_tail + 1]
            )
            # return new location of the pivot val
            return lower_side_tail + 1

        # init case:
        if high is None:
            return self.quicksort(low=0, high=len(self.collection) - 1)
        # recursive case
        elif high - low > 0:
            # A: DIVIDE: choose a pivot 
            pivot = high
            # B: CONQUER: partition the list around the pivot
            sorted_pivot = partition(pivot)
            # C: COMBINE: recurse the process on both sides of the pivot
            self.quicksort(low, sorted_pivot - 1)
            self.quicksort(sorted_pivot + 1, high)

    """
               0  1  2  3  4
    Example: [-5, 3, 4, 7, 6]
                        s  pv
                 lst
    low     |      high     |      pivot ```` ```````````````pivot          lst         swappper             
     0      |      None     |       
     0              4               4   ---> partition    :    4        |   -1              0
                                                                             0              1
                                                                             1              2
                                                                                            3
                                                                                            4
    """

    def bucket_sort(self):
        pass


if __name__ == "__main__":
    array = [3, -5, 6, 7, 4]
    arr = ArrayList(array)
    print("Before sorting: ", arr.collection)
    arr.quicksort()
    print("After sorting: ", arr.collection)