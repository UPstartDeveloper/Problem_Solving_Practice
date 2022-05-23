from list import LinkedList


class ArrayStack:
    """last index is the top"""

    def __init__(self):
        self.stack = list()

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def push(self, new):
        self.stack.append(new)


class LinkedStack:
    """top of the stack is the head node"""

    def __init__(self):
        self.items = LinkedList()

    def top(self):
        head_node = self.items.head
        if head_node:
            return head_node.val

    def pop(self):
        head = self.items.head
        deleted = self.items.delete(head)
        if deleted:
            return deleted.val

    def push(self, new):
        new_node = list.ListNode(new)
        self.items.add(new_node, front=True)
