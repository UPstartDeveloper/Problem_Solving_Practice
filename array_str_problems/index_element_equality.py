def index_equals_value_search(arr, use_linear=False):
  
    def _linear():
        for index, elem in enumerate(arr):
            if index == elem:
                return index
        return -1
  
    def _binary_search():
        """
        iterative Binary Searrch
        - start at the middle
        - go left/right based on how middle val compares to its index
        - O(log(n)) time, O(1) space
        """
        low, hi = 0, len(arr) - 1

        while low <= hi:
            # do the BS
            middle = (low + hi) // 2
            mid_elem = me = arr[middle]

            # base case: found!
            if middle == me:
                return middle

            # recursive cases
            elif middle > me:
                low = middle + 1

            else:  # middle < me:
                hi = middle - 1

        # base case: not found!
        return -1
  
    if use_linear:
        return _linear()
    return _binary_search()
