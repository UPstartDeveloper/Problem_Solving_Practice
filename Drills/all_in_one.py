# ARRAYS

from typing import List

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

# Stacks and Queues
class ArrayStack(Array):
    '''top is the last index'''

    def __init__(self, array):
        super().__init__(array)

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def push(self, item):
        self.items.append(item)

    
class ArrayQueue(Array):
    '''first index of the array is the front of queue'''
    def __init__(self, array):
        super().__init__(array)

    def enqueue(self, item: int):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def front(self):
        if len(self.items) > 0:
            return self.items[0]


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item: ListNode):
        if self.head is None:
            self.head = self.tail = self.item
        else:
            self.tail.next = item
            self.tail = item
    
    def prepend(self, item: ListNode):
        if self.head is None:
            self.head = self.tail = item
        else:
            item.next = self.head
            self.head = item

    def length(self):
        num_nodes = 0
        runner = self.head
        while runner is not None:
            num_nodes += 1
            runner = runner.next
        return num_nodes

    def find(self, item: int) -> List[ListNode, ListNode]:
        '''returns the node with a given item, and the one before it'''
        prev = None
        runner = self.head

        while runner.key != item:
            prev = runner
            runner = runner.next

        return [runner, prev]

    def delete(self, item):
        deleted_item, item_before = self.find(self.tail.key)
        
        if item_before is not None:
            item_before.next = deleted_item.next
        else:   # head is being deleted
            self.head = self.tail = None
        
        # if tail is being deleted
        if deleted_item == self.tail:
            self.tail = item_before
        
        return deleted_item

    
class LinkedStack(LinkedList):
    '''the tail is the top of the stack'''
    def __init__(self):
        super().__init__()

    def peek(self):
        if self.tail is not None:
            return self.tail.key
        
    def push(self, item: int):
        self.append(ListNode(item))

    def pop(self):
        if self.tail is not None:
            self.delete(self.tail.key)


class LinkedQueue(LinkedList):
    '''the head is the front'''
    def __init__(self):
        super().__init__()

    def front(self):
        if self.head is not None:
            return self.head.key

    def enqueue(self, item):
        self.append(ListNode(item))

    def dequeue(self):
        if self.head is not None:
            self.delete(self.head.item)
