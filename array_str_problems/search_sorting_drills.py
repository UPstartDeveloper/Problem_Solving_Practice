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


if __name__ == "__main__":
    array = Array([4, 5, 9, 7, 3, 1, 8])
    array.quick_sort()
    print(array.arr)
