"""
CtCI 7.9 CircularArray:
Implement a CircularArray class that supports an 
array-like data structure which can be efficiently rotated. 

If possible, the class should use a generic type (also called a template), 
and should support iteration via the standard 
    - for (Obj 0 : circularArray) notation.


1. Scope:
    - Why - List ADT
    - What - last item ----> first item, 2nd, 3rd, ...
    - Who - developers
    - Where - ?
    - How? 

2. Core Objects:

    CircularArray
        - items - all elements in arr
        - head, tail pointers
        - methods:
            append, prepend, find, remove, print_all, replace
    Object
        - cyclical linked list
        - .val, .next pointers

    CA ---> Object

3. TODO:
    - implement DLL (TODO: tail.next = head?)
    - implement the iterator protocol

"""
from typing import Optional

class DoublyNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = DoublyNode(None), DoublyNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, item: DoublyNode) -> None:
        if isinstance(item, DoublyNode):
            item.next = self.tail
            item.prev = self.tail.prev
            self.tail.prev.next = item
            self.tail.prev = item
            self.size += 1

    def prepend(self, item: DoublyNode) -> None:
        """No error if input item is not a valid DoublyNode"""
        if isinstance(item, DoublyNode):
            item.prev = self.head
            item.next = self.head.next
            self.head.next.prev = item
            self.head.next = item
            self.size += 1

    def _search(self, val) -> Optional[DoublyNode]:
        node = self.head.next
        while node != self.tail and node.val != val:
            node = node.next
        # not found
        if node == self.tail:
            return None
        # found
        return node

    def find(self, val) -> Optional[DoublyNode]:
        return self._search(val)

    def remove(self, val) -> Optional[DoublyNode]:
        """if node not found, no changes made. fails silently."""
        node = self._search(val)
        # move pointers around, and decrement size
        if node is not None:
            previous, upcoming = node.prev, node.next
            previous.next = node.next
            upcoming.prev = node.prev
            self.size -= 1


class CircularArray:
    def __init__(self):
        self.items = DoublyLinkedList()
        self.items.head.prev = self.items.tail
        self.items.tail.next = self.items.head

    def add(self, val: int, add_last=True):
        pass

    def __iter__(self):
        self.current_node = self.items.head.next
        return self

    def __next__(self):
        if self.current_node is not self.items.tail:
            # copy value to return 
            next_val = self.current_node.val
            # move on
            self.current_node = self.current_node.next
            # return!
            return next_val
        else:  # reached the end
            raise StopIteration
