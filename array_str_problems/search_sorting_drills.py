class Array:
    def __init__(self, items=[]):
        self.arr = items

    def linear_search(self, target, use_iteration=True):
        '''Returns None if not found, or else index'''

        def _linear_search_recursive(index=0):
            '''Linear time and space'''
            # Base Case - past the end of the array
            if index < len(self.arr):
                # look for the item
                item = self.arr[index]
                # found
                if item == target:
                    return index
                # not found - recursive case
                return _linear_search_recursive(index + 1)
            return None
        
        def _linear_search_iterative():
            '''linear time and constant space'''
            for index, item in enumerate(self.arr):
                if item == target:
                    return index
            return None
        
        if use_iteration is True:
            return _linear_search_iterative()
        return _linear_search_recursive()

    def binary_search(self, target, use_iteration=True):
        """Assumes the array is already sorted. Returns None if not found.
        Clarifiying Question:
        - which should we return if there are duplicates of the same element?
        Code Traces:

        Rules:
        using low <= high is fine

        1. 
            0 1  2  3  4  5  6  7
        [-5, -5, 6, 7, 7, 8, 9, 10], target = 9 ✅
         l          m           h
                       l  m     h
                            l   h
         --------------------------
         l          m           h   target = -5 ✅
         l    m    h
         --------------------------
         l          m           h   target = -7 ✅
         l    m    h
      l, h, m
        --------------------------
         l          m           h   target = 12 ✅
                       l  m     h
                          l,m   h
                               l,h

        """

        def _binary_search_iterative():
            '''O(log n) time, constant space'''
            # init low, high
            low, high = 0, len(self.arr) - 1
            # TODO: test if it should be </<=
            while low <= high:
                # index the middle
                mid_ndx = (low + high) // 2
                mid = self.arr[mid_ndx]
                # target found
                if mid == target:
                    return mid_ndx
                # go to the left
                elif target < mid:
                    high = mid_ndx - 1
                # go to the right side
                elif target > mid:
                    low = mid_ndx + 1
            # not found
            return None

        def _binary_search_recursive(low=0, hi=None):
            '''O(log n) time and space'''
            # init params
            if hi is None:
                hi = len(self.arr) - 1
            # get the middle
            mid = (low + hi) // 2
            mid_elem = self.arr[mid]
            # found
            if target == mid_elem:
                return mid
            # not found
            elif low > hi:
                return None
            # search the left side
            elif target < mid_elem:
                return _binary_search_recursive(low, mid - 1)
            # search the right side
            elif target > mid_elem:
                return _binary_search_recursive(mid + 1, hi)
            
 
        if use_iteration is True:
            return _binary_search_iterative()
        return _binary_search_recursive()

    def quick_sort(self, low=0, high=None):
        """
        Divide - pick a pivot
        Conquer - swap elements about the pivot
        Combine - recursive the process on the left and right
         0  1  2  3  4  5  6
        [4, 5, 9, 7, 3, 1, 8]
               ^  ^     ^
        [4, 5, 1, 7, 3, 9, 8]        [4, 5, 1, 7, 3, 9, 8]
                  ^                            ^     ^       
                  ^  ^                            ^
        [4, 5, 1, 3, 7, 9, 8]
                  ^
                  ^  
                  ^
         0  1  2
        [4, 5, 1]
            ^  ^
            ^
        [4, 1, 5]
            ^  
            ^
            ^


        l   h   p   left    right
        0   N   3   0->3    6-> 3
            6   3
        0   2   1     0       2
        """

        def partition(low, high):
            # (arbitrarily choose the last element as the pivot)
            pivot = self.arr[high]
            # keep two pointers to help find the sorted pos of pivot
            lower_side_tail, swapper = low - 1, low
            while swapper < high:
                # move lower elements to left side
                if self.arr[swapper] <= pivot:
                    # move the other pointer to the last element < pivot
                    lower_side_tail += 1
                    # swap - throw the new lower element we've found backwards
                    self.arr[swapper], self.arr[lower_side_tail] = (
                        self.arr[lower_side_tail], self.arr[swapper]
                    )
                # move on to check the next element
                swapper += 1
            # move the pivot into its sorted position
            self.arr[lower_side_tail + 1], self.arr[high] = (
                self.arr[high], self.arr[lower_side_tail + 1]
            )
            # return the pivots sorted index
            return lower_side_tail + 1

        # Divide - pick a pivot
        if high is None:
            high = len(self.arr) - 1
        # Conquer - swap elements about the pivot
        pivot = partition(low,  high)
        # Combine - recursive the process on the left and right side
        if pivot - low >= 2:
            self.quick_sort(low, pivot - 1)
        if high - pivot >= 2:
            self.quick_sort(pivot + 1, high)

    def _is_sorted(self) -> bool:
        '''Linear Search to determine if an array is in ascending order.'''
        index = 0
        while index < len(self.arr) - 1:
            elem, elem_after = self.arr[index], self.arr[index + 1]
            if elem_after < elem:
                return False
            index += 1
        return True

    def bubble_sort(self):
        """Stable, in-place sorting algoritm that runs in quadratic time 
        and constant space.

        can only guarantee that one unsorted elem moves into sorted position
        per each pass ==> O(n^2) time
        Code Trace:
         0  1  2  3  4  5  6
        [1, 3, 4, 5, 7, 8, 9]
                           i 

        s = 0
        """
        # init the number of swaps
        swaps = -1
        # we'll break when we can pass over having done no swaps
        while swaps != 0:
            swaps_made = 0
            # iterate over the array
            index = 0
            while index < len(self.arr) - 1:
                # swap out of place elements
                elem, elem_after = self.arr[index], self.arr[index + 1]
                if elem_after < elem:
                    self.arr[index], self.arr[index + 1] = (
                        elem_after, elem
                    )
                    # make sure to keep track of the swaps
                    swaps_made += 1
                # move ahead in the array regardless
                index += 1
            swaps = swaps_made
        

def quick_sort_out_of_place(array):
    """Recursive QuickSort Implementation:
    - O(nlog(n)) time
    - O(n) space (out of place)
    - unstable
    - pivot = mean of the range (best on normal, numerical distributions)
    """
    # Base Case
    if len(array) < 2:
        return array
    # Recurisive Case - choose a pivot
    pivot = (min(array) + max(array)) // 2
    # Divide and Conquer - partition by the pivot
    lower_partition = [val for val in array if val < pivot]
    middle = [val for val in array if val == pivot]
    upper_partition = [val for val in array if val > pivot]
    # combine - recurse on left and right partitions
    return (
        quick_sort_out_of_place(lower_partition) + 
        middle + 
        quick_sort_out_of_place(upper_partition)
    )


if __name__ == "__main__":
    array = Array([4, 5, 9, 7, 3, 1, 8])
    array.quick_sort()
    print(array.arr)
    array2 = [6, 4, 5, 6, 7, -3, 8, 1]
    print(quick_sort_out_of_place(array2))
