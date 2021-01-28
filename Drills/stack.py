class ListNode:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self, top):
        self.top = top

    def push(self, node):
        '''Adds the new node to the top of the stack - PREPEND'''
        node.next = self.top
        self.top = node

    def pop(self):
        """
        return the head of the list
        """
        old_top = self.top
        self.top = self.top.next
        return old_top

    def peek(self):
        return self.top.data


class ArrayStack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]