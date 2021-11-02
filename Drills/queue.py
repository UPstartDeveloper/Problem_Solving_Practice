class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back
        if self.front is not None:
            self.front.next = self.back

    def front(self):
        """return the value at the front of the queue"""
        if self.front:
            return self.front.data
        else:
            return None

    def enqueue(self, item):
        """add an item to the back of the queue"""
        # if no previous nodes, set both the front and back
        if not self.back:
            self.front = item
            self.front.next = self.back
        # if the back is already there, update the back
        else:
            self.back.next = item
        self.back = item

    def dequeue(self):
        """Remove and return the item at the front of the queue"""
        old_front = self.front
        if self.front:
            self.front = self.front.next
        return old_front


class ArrayQueue:
    """The front is index 0, and the last index is the back"""

    def __init__(self):
        self.items = list()

    def front(self):
        if len(self.items) > 0:
            return self.items[0]
        return None

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        return None
