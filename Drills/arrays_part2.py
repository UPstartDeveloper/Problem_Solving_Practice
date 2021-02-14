class Array:
    def __init__(self, items: list):
        self.items = items

    """Searching Algorithms on Arrays"""
    def _linear_search_iterative(self, value):
        '''O(n) time, O(1) space'''
        for index, item in enumerate(self.items):
            if item == value:
                return index

        return -1

    def _linear_search_recursive(self, value, index=0):
        '''O(n) time and space'''
        if index < len(self.items):
            # Base Case --> item found
            if self.items[index] == value:
                return index
            # Recursive Case --> move on to the next item
            return self._linear_searhc_recursive(value, index + 1)
        # Base Case --> item not found 
        return -1

    def search_linear(self, value, use_iterative=True):
        if use_iterative is True:
            return self._linear_search_iterative(value)
        return self._linear_search_recursive(value)

    def _binary_search_iterative(self, target):
        '''O(log n) time, O(1) space'''
        # init the middle index
        low = 0
        high = len(self.items) - 1
        # check the middle over and over
        while low <= high:
            mid = (low + high) // 2
            mid_val = self.items[mid]
            # found
            if target == mid_val:
                return mid
            # go to the left (mid > target value)
            elif target < mid_val:
                high = mid - 1
            # go to the right (mid < target value)
            elif target > mid_val:
                low = mid + 1
        # not found
        return -1

    def _binary_search_recursive(self, target, low=0, high=None):
        '''O(log n) space, O(log n) time'''
        if high is None:
            high = len(self.items) - 1
        mid_ndx = (low + high) // 2
        mid_val = self.items[mid_ndx]
        # Base Cases - found and not found
        if target == mid_val:
            return mid_ndx
        elif low > high:
            return -1
        # go right
        elif target < mid_val:
            return self._binary_search_recursive(mid_ndx + 1, high)
        # go left
        else:
            return self._binary_search_recursive(low, mid_ndx - 1)

    def search_binary(self, value, use_iterative=True):
        '''Values array must be sorted'''
        if use_iterative is True:
            return self._binary_search_iterative(value)
        return self._binary_search_recursive(value)

    """Sorting Algorithms on Arrays"""

    def _bubble_sort(self) -> None:
        '''O(n^2) time; O(1) space b/c this is a mutative sorting algorithm'''
        # pass over the array
        is_sorted = False
        while is_sorted is False:
            swaps = 0
            for index in range(len(self.items) - 1):
                # make any swaps (and increment count of swaps)
                value, next_value = self.items[index], self.items[index + 1]
                if next_value < value:
                    self.items[index], self.items[index + 1] = next_value, value
                    swaps += 1
            is_sorted = (swaps == 0)

    def _insertion_sort(self) -> None:
        # insert every element into the "sorted portion"
        for insert_element_pos in range(1, len(self.items)):
            insert_elem = self.items[insert_element_pos]
            # search the array for this element's correct position
            current_pos = insert_element_pos
            for index_before in range(insert_element_pos - 1, -1, -1):
                elem_before = self.items[index_before]
                # swap if necessary:
                if elem_before > insert_elem:
                    self.items[index_before], self.items[current_pos] = (
                        insert_elem, elem_before
                    )
                    # update the index where the insertion element is now
                    current_pos = index_before

    def _merge_sort(self, array=None) -> list:
        ##### Helper Function
        def _merge(left, right) -> list:
            index_left, index_right = 0, 0
            sorted = list
            # decide the order in which the elements from both halves combine
            while index_left < len(left) and index_right < len(right):
                elem_left, elem_right = left[index_left], right[index_right]
                if elem_left <= elem_right:
                    sorted.append(elem_left)
                    index_left += 1
                else:  # elem_right < elem_left
                    sorted.append(elem_right)
                    index_right += 1
            # add any remaining elements
            if index_left < len(left):
                for index in range(index_left, len(left)):
                    sorted.append(left[index])
            elif index_right < len(right):
                for index in range(index_right, len(right)):
                    sorted.append(right[index])
            # return the array
            return sorted 
        ##### Driver Code
        if array is None:
            array = self.items
        # Base Case: array is less than 2 elements long
        if len(array) < 2:
            return array 
        # Divide the Array at the middle
        mid = len(array) // 2
        # Conquer - sort both halves
        left = self._merge_sort(array[:mid])
        right = self._merge_sort(array[mid:])
        # Combine - merge the two halves together 
        return _merge(left, right)

    def _quick_sort(self,low=0, high=None) -> list:
        '''mutative, divide and conquer sorting algorithm'''
        if high is None:
            high = len(self.items) - 1
        # Divide the list - choose the middle element as the pivot
        pivot = (low + high) // 2
        # Conquer - partition the elements about the pivot
        pivot_elem = self.items[pivot]
        left = low
        right = high
        while right > left:
            while left < right and self.items[left] <= pivot_elem:
                left += 1
            while right > left and self.items[right] > pivot_elem:
                right -= 1
            # swap the pointers on the left and right side
            if 0 < left < len(self.items) and 0 < right < len(self.items):
                self.items[left], self.items[right] = (
                    self.items[right], self.items[left]
                )
        # Recurse - repeat the process on the left and right sides
        self._quick_sort(low, pivot - 1)
        self._quick_sort(pivot + 1, high)
        # return the array
        return self.items

    def sort(self, mutate=True, fast=True):
        if mutate is True:
            if fast is True:
                self._quick_sort()
            else:
                self._insertion_sort()
                # self._bubble_sort()
            return self.items
        else:  # use a non-mutative algoritm
            return self._merge_sort()


class ArrayStack(Array):
    '''The top of this stack is the last element'''
    def __init__(self, items: list):
        super().__init__(items)

    def peek(self):
        # guard clause
        assert len(self.items) > 0, "There are no items in the stack"
        return self.items[-1]

    def push(self, item):
        self.append(item)

    def pop(self):
        assert len(self.items) > 0, "There are no items to pop"
        return self.items.pop()


class ArrayQueue(Array):
    """The front of the queue is index 0, the back is the last index"""

    def __init__(self, items: list):
        super().__init__(items)

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        assert len(self.items) > 0, "There are no items to display."
        return self.items[0]

    def dequeue(self):
        assert len(self.items) > 0, "There are no items to dequeue."
        return self.items.pop(0)


if __name__ == "__main__":
    # Test out the sorting algorithms
    items = [-7, 6, 4, 2, -7, 5, 3, 1, 2]
    array = Array(items)
    print(f"Before sorting: {items}")
    array.sort()
    print(f"After Sorting: {items}")
