# ARRAYS


class Array:
    def __init__(self, array):
        self.items = array
    '''Search Algorithms'''
    def linear_search(self, target):
        '''linear time, constant space'''
        for ndx, item in enumerate(self.items):
            if target == item:
                return ndx
        return None

    def linear_search_recursive(self, target, ndx=0):
        '''linear time and space'''
        if ndx < len(self.items):
            item = self.items[ndx]
            if item == target:
                return ndx
            else:
                return self.linear_search_recursive(x, ndx + 1)
        return None

    def bin_search_iterative(self, target):
        """self.items is assumed to be sorted in ascending order.
           logarithmic time, constant space"""
        lo = 0
        hi = len(self.items) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_elem = self.items[mid]

            if target == mid_elem:
                return mid
            elif target < mid_elem:
                hi = mid - 1
            elif target > mid_elem:
                low = mid + 1
        # not found 
        return None

    def bin_search_recursive(self, target, lo=0, hi=None):
        """logarithmic time and space"""
        if hi is None:
            hi = len(self.items) - 1
        mid = (lo + hi) // 2
        mid_elem = self.items[mid]

        if target == mid_elem:
            return mid
        elif lo > hi:
            return None
        elif target < mid_elem:
            return self.bin_search_recursive(lo, mid - 1)
        elif target > mid_elem:
            return self.bin_search_recursive(mid + 1, hi)

    '''Sorting Algorithms'''

    def insertion_sort(self) -> None:
        """this method is mutative - stable, internal, quadratic time, constant space
        - good for when you need something stable, you know the data can fit into RAM
        - and when you know it might be nearly sorted already
        """
        # first ndx is already sorted 
        for index in range(1, len(self.items)):
            # grab the element at the current index
            to_insert = self.items[index]
            to_insert_index = index
            # insert it into the proper position in the sorted part
            for index_before in range(index, -1, -1):
                elem_before = self.items[index_before]
                # swap if necessary 
                if elem_before > to_insert:
                    self.items[index_before], self.items[to_insert_index] = (
                        to_insert, elem_before
                    )
                    # update the index where the elem to insert is
                    to_insert_index = index_before

    def merge_sort(self):
        '''out of place, loglinear time'''
        pass

    def counting_sort(self):
        '''linear time (n + k, where k is the difference between min and max),
        out of place, works only with integer values
        - good for when you know beforehand the values are in a certain range
        - and that the dataset is not sparse (e.g. human ages in the Census data)
        '''

        min_elem = min(self.items)
        max_elem = max(self.items)

        frequencies = [0 for _ in range(max - min)]

        for item in self.items:
            index = item - min_elem
            frequencies[index] += 1

        sorted = list()
        for elem, count in enumerate(frequencies):
            sorted.extend([elem for _ in range(count)])

        return sorted
