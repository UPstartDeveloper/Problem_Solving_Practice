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
