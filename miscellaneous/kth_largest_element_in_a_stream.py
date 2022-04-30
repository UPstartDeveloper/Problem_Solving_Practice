from typing import List


class BinaryMinHeap:
    def __init__(self, items=None):
        """Initialize this heap"""
        # Initialize an empty list to store the items
        self.items = []
        if items:
            for item in items:
                self.insert(item)

    def size(self):
        """Return the number of items in this heap."""
        return len(self.items)

    def insert(self, item):
        # Insert the item at the end and bubble up to
        self.items.append(item)
        if self.size() > 1:
            self._bubble_up(self._last_index())

    def delete_min(self):
        assert self.size() > 1
        max_item = self.items[0]
        # Move the last item to  root and bubble down
        last_item = self.items.pop()
        self.items[0] = last_item
        if self.size() > 1:
            self._bubble_down(0)
        return max_item

    def _bubble_up(self, index):
        # Get the item's value
        item = self.items[index]
        # Get the parent's index and value
        parent_index = self._parent_index(index)
        parent_item = self.items[parent_index]
        # Swap this item  if values are out of order
        if item < parent_item:
            self.items[index], self.items[parent_index] = (parent_item, item)
            # Recursively bubble up again if necessary
            if parent_index > 0:
                new_parent_index = self._parent_index(parent_index)
                if item < self.items[new_parent_index]:
                    self._bubble_up(parent_index)

    def _bubble_down(self, index):
        # Get the index of the item's left and right children
        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)
        last = self._last_index()
        if left_index > last:
            return  # This index is a leaf
        # Get the item's value
        item = self.items[index]
        # Determine which child item to compare this node to
        child_index = left_index
        # check if indicies valid first
        if right_index <= last:
            if self.items[right_index] < self.items[left_index]:
                child_index = right_index
        # Swap this item with a child item
        child_item = self.items[child_index]
        if item > child_item:
            self.items[index], self.items[child_index] = (child_item, item)
            return self._bubble_down(child_index)

    def _last_index(self):
        return len(self.items) - 1

    def _parent_index(self, index):
        if index <= 0:
            raise IndexError(
                "Heap index {} has no parent \
                index".format(
                    index
                )
            )
        return (index - 1) >> 1  # Shift right to divide by 2

    def _left_child_index(self, index):
        """Return the left child index"""
        return (index << 1) + 1  # Shift left to multiply by

    def _right_child_index(self, index):
        """Return the right child index"""
        return (index << 1) + 2  # Shift left to multiply by


class KthLargest:
    """https://leetcode.com/problems/kth-largest-element-in-a-stream/"""

    def __init__(self, k: int, nums: List[int]):
        # make a min heap of the largest k elems
        self.size_limit = k
        self.heap = BinaryMinHeap(nums[:k])
        for num in nums[k:]:
            self.add(num)

    def add(self, val: int) -> int:
        # if the new val is higher than the root of the heap
        if len(self.heap.items) < self.size_limit or val > self.heap.items[0]:
            self.heap.insert(val)
        if len(self.heap.items) > self.size_limit:
            self.heap.delete_min()
        #  return whatever the new kth largest is
        return self.heap.items[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
