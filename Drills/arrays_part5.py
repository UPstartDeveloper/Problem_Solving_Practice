from typing import List


class Array:
    def __init__(self, items: List[int]):
        self.nums = items

    def search_linear(self, target, use_iteration=True):
        def _iterative():
            # iterative
            for index, num in enumerate(self.nums):
                # found
                if num == target:
                    return index
            # not found
            return -1

        def _recursive(index=0):
            if index < len(self.items):
                # found
                if self.items[index] == target:
                    return index
                return _recursive(index + 1)
            # not found
            return -1

        if use_iteration:
            return _iterative()
        return _recursive()

    def search_binary(self, target, use_iterative=True):
        """ASSUME self.items is sorted"""

        def _iterative():
            low, hi = 0, len(self.items) - 1
            while low <= hi:
                mid_ndx = (low + hi) // 2
                mid_elem = self.items[mid_ndx]
                # found
                if target == mid_elem:
                    return mid_ndx
                # move left
                elif target < mid_elem:
                    hi = mid_ndx - 1
                # move right
                else:  # target > mid_elem
                    low = mid_ndx + 1
            # not found
            return -1

        def _recursive(low=0, hi=len(self.items) - 1):
            # not found
            if low > hi:
                return -1
            # calculate the middle
            mid_ndx = (low + hi) // 2
            mid_elem = self.items[mid_ndx]
            # found
            if target == mid_elem:
                return mid_ndx
            # move left
            elif target < mid_elem:
                return _recursive(low, mid_ndx - 1)
            # move right
            else:  # target > mid_elem
                return _recursive(mid_ndx + 1, hi)

        if use_iterative:
            return _iterative()
        return _recursive()

    def bubble_sort(self):
        is_sorted = False
        while is_sorted is False:
            swaps, ndx = 0, 0
            while ndx < len(self.items) - 1:
                next_ndx = ndx + 1
                elem, next_elem = self.items[ndx], self.items[next_ndx]
                # swap if needed
                if elem > next_elem:
                    self.items[next_ndx], self.items[ndx] = elem, next_elem
                    swaps += 1
                # move on
                ndx += 1
            # update is sorted
            if swaps == 0:
                is_sorted = True
        # all done!
        return self.items

    def insertion_sort(self):
        # assume first is sorted
        ndx = 1
        # move each subseq ndx in sorted order
        while ndx < len(self.items):
            # swaps occur - use two pointers
            current_ndx = ndx
            while current_ndx > 0:
                prev_ndx = current_ndx - 1
                # see if these 2 elems need to swap
                current, prev = self.items[current_ndx], self.items[prev_ndx]
                if prev_ndx > -1 and prev > current:
                    # swap
                    self.items[prev_ndx], self.items[current_ndx] = current, prev
                # complete the swapping by moving back
                current_ndx -= 1
            # move on to sorting next elem
            ndx += 1
        # all done!
        return self.items
