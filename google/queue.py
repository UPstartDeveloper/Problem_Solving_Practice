from doubly import DLL, DoublyNode
from list import LinkedList, ListNode


class ArrayQueue:
    """going to choose the last index and the back, and first as front
       in prod this choice would most likely depend on the application domain
    """
    def __init__(self):
        self.items = list()

    def enqueue(self, new):
        self.items.append(new)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)

    def front(self):
        if self.items:
            return self.items[0]


class LinkedQueue:
    """front of the queue is the head, back is the tail"""
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, new):
        new_node = ListNode(new)
        self.items.add(new_node, front=False)

    def dequeue(self):
        if self.items.size > 0:
            first = self.items.head
            deleted = self.items.delete(first)
            if deleted is not None:
                return deleted.val

    def front(self):
        if self.items.size > 0:
            return self.items.head.val


class Deque:

    def __init__(self):
        self.items = DLL()

    def front(self):
        if self.items.size > 0:
            return self.items.head.next.val

    def back(self):
        if self.items.size > 0:
            return self.items.tail.prev.val

    def enqueue(self, new_val, add_front=False):
        self.items.add(new_val, add_last=(not add_front))

    def dequeue(self, front=True):
        if self.items.size > 0:

            if front:
                target = self.items.head.next
            else:
                target  = self.items.tail.prev

            return self.items.delete(target.val)
            
            
