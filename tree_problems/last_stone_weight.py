class BinaryMaxHeap:
    """Source: https://github.com/UPstartDeveloper/CS-2.1-Trees-Sorting/blob/master/Code/priorityqueue.py"""

    def __init__(self, items=None):
        """Initialize this heap and insert the given items, if any."""
        # Initialize an empty list to store the items
        self.items = []
        if items:
            for item in items:
                self.insert(item)

    def size(self):
        """Return the number of items in this heap."""
        return len(self.items)

    def insert(self, item):
        # Insert the item at the end and bubble up to the root
        self.items.append(item)
        if self.size() > 1:
            self._bubble_up(self._last_index())

    def delete_max(self):
        assert self.size() > 1
        max_item = self.items[0]
        # Move the last item to the root and bubble down to the leaves
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
        # Swap this item with parent item if values are out of order
        if item > parent_item:
            self.items[index], self.items[parent_index] = parent_item, item
            # Recursively bubble up again if necessary
            if parent_index > 0:
                new_parent_index = self._parent_index(parent_index)
                if item > self.items[new_parent_index]:
                    self._bubble_up(parent_index)

    def _bubble_down(self, index):
        # Get the index of the item's left and right children
        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)
        last = self._last_index()
        if left_index > last:
            return  # This index is a leaf node (does not have any children)
        # Get the item's value
        item = self.items[index]
        # Determine which child item to compare this node's item to
        child_index = left_index
        # check if indicies valid first
        if right_index <= last:
            if self.items[right_index] > self.items[left_index]:
                child_index = right_index
        # Swap this item with a child item if values are out of order
        child_item = self.items[child_index]
        if item < child_item:
            self.items[index], self.items[child_index] = child_item, item
            return self._bubble_down(child_index)

    def _last_index(self):
        """Return the last valid index in the underlying array of items."""
        return len(self.items) - 1

    def _parent_index(self, index):
        """Return the parent index of the item at the given index."""
        if index <= 0:
            raise IndexError("Heap index {} has no parent index".format(index))
        return (index - 1) >> 1  # Shift right to divide by 2

    def _left_child_index(self, index):
        """Return the left child index of the item at the given index."""
        return (index << 1) + 1  # Shift left to multiply by 2

    def _right_child_index(self, index):
        """Return the right child index of the item at the given index."""
        return (index << 1) + 2  # Shift left to multiply by 2


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        LeetCode: https://leetcode.com/problems/last-stone-weight/
        
        Input:
            int[len > 0, elem > 0, dupes, unsorted]
        
        Output:
            0 or value that's left
            
        Intuition:
            max heap
            sorting techniques?
            
        EC:
            invalid input
                []? neg, 0 weight ---> ValueError?
                
        Approach:
         n = len(stones)
         k = # of stones smashed = 2
        
            1) Heap ---> O(n log n)
                A: heapify the array at the start - O(n log n)
                
                B: game loop ---> while len > 1:  ---> O(n log n)
                    
                    C: dequeue twice
                    
                    D: find the min
                    
                    E: subtract the min from both
                    
                    F: whatever the updated values are
                        re-enqueue it if it's > 0
                        
                C: return 0 or value that's left
                
        2) Heap --> O(n * n log(k))
                EC: 1 elem --> output fast 
                
                A: 2 linear passes --> rm the top 2 elems in a min heap
                
                B: game loop ---> for n times:  [TODO[test]]
                    
                    C: fill the buffer - if we need to (keep ptr to the indicies)
                        only consider weights > 0, grester than the root 
                        put in (elem, index)
                    
                    D: find the min - top of min heap, also empty the other
                    
                    E: subtract the min from both
                    
                    F: whatever the updated values are
                        re-append to the array it if it's > 0
                        
                C: return 0 or value that's left
                
         3) max Heap ---> O(n log n)
            A: sort the array - O(n log n)

            B: game loop ---> for loop:  ---> O(n log n)

                C: take two from the back

                D: find the min

                E: subtract the min from both

                F: whatever the updated values are
                    re-enqueue it if it's > 0

            C: return 0 or value that's left
        
        """
        # A: heapify the array at the start - O(n log n)
        heap = BinaryMaxHeap(stones)

        # B: game loop ---> while len > 1:  ---> O(n log n)
        while heap.size() > 1:

            # C: dequeue twice
            larger = heap.delete_max()
            smaller = heap.delete_max()

            # E: subtract the min from both - we already know smaller -> 0 tho
            new_large = larger - smaller

            # F: update the heap
            if new_large > 0:
                heap.insert(new_large)

        # C: return 0 or value that's left
        if heap.size() > 0:
            return heap.get_max()
        return 0
