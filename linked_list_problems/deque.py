from typing import List


class DoublyNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, items: List[int]):
        self.head = DoublyNode(None)
        self.tail = DoublyNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        for item in items:
            self.add(item)

    def add(self, item, append_last=True):

        ## HELPERS
        def _append(node):
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node

        def _prepend(node):
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node

        ## DRIVER
        new_node = DoublyNode(item)
        if append_last:
            _append(new_node)
        else:
            _prepend(new_node)
        self.size += 1

    def _find_node(self, item_val) -> DoublyNode:
        node = self.head
        while node and node.val != item_val:
            node = node.next
        return node

    def delete(self, item_val) -> DoublyNode:
        if item_val is not None:  # valid input
            node = self._find_node(item_val)
            if node is not None:  # node val found
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
                return node


class Deque:
    def __init__(self):
        """The front is the head of DLL, back is tail"""
        self.items = DoublyLinkedList()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self, item) -> int:
        if self.items.size > 0:
            first_val = self.items.head.next.val
            return self.items.delete(first_val).val
        return None

    def front(self) -> int:
        if self.items.size > 0:
            return self.items.head.next.val
        return None
