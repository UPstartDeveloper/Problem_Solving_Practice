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
            # pick the middle of the range as the pivot
            pivot = (low + high) // 2
            # swap left and right elements into order
            left, right = low, high
            while left < right:
                while left < high and self.arr[left] < self.arr[pivot]:
                    left += 1
                while right > left and self.arr[right] > self.arr[pivot]:
                    right -= 1
                # swap
                if left < right:
                    self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
                    left, right = right, left
            # return the pivot inde
            return pivot

        # Divide - pick a pivot
        if high is None:
            high = len(self.items) - 1
        # Conquer - swap elements about the pivot
        pivot = partition(low,  high)
        # Combine - recursive the process on the left and right side
        self.quick_sort(low, pivot)
        self.quick_sort(pivot + 1, high)
