class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None  # TODO[required?]
        self.size = 0

    def add(self, new_node, front=True):

        ### HELPERS
        def _prepend(node):
            if self.head is None:
                self.tail = node
            node.next = self.head
            self.head = node

        def _append(node):
            if self.head is None:
                self.head = node
            else:
                self.tail.next = node
            self.tail = node  # for a list of size 1 --> head = tail

        ### DRIVER
        if front is True:
            _prepend(new_node)
        else:
            _append(new_node)
        self.size += 1

    def _find(self, node):
        prev, current = None, self.head
        while current and current.val != node.val:
            prev = current
            current = current.next
        return prev, current

    def search(self, node):
        _, found = self._find(node)
        return found  # ListNode or None

    def update(self, node, new_node):
        prev, found = self._find(node)
        # updating in general
        if prev is not None:
            prev.next = new_node
        if found is not None:
            new_node.next = found.next
            # updating the head
            if found == self.head:
                self.head = new_node
            # updating the tail
            if found == self.tail:
                self.tail = new_node

    def delete(self, node):
        prev, found = self._find(node)
        if found is not None and prev:
            prev.next = found.next

        if found and found == self.head:
            self.head = None

        if found and found == self.tail:
            self.tail = prev
            self.tail.next = None

        self.size -= 1

    def items(self):
        all_values, node = list(), self.head

        while node is not None:
            all_values.append(node.val)
            node = node.next

        return all_values
