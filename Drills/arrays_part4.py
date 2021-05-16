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

    def merge_sort(self):
        pass

    def quicksort(self):
        pass

    def bucket_sort(self):
        pass