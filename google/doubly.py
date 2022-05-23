class DoublyNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self):
        self.head = DoublyNode(val=None)
        self.tail = DoublyNode(val=None)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, new_val, add_last=True):
        def _append(node):
            node.prev = self.tail.prev
            node.next = self.tail

            self.tail.prev.next = node
            self.tail.prev = node

        def _prepend(node):
            node.prev = self.head
            node.next = self.head.next

            self.head.next.prev = node
            self.head.next = node

        new_node = DoublyNode(new_val)
        if add_last:
            _append(new_node)
        else:
            _prepend(new_node)
        self.size += 1

    def _search(self, val):
        node = self.head.next
        while node != self.tail and node.val != val:
            node = node.next
        return node

    def find(self, val):
        found_node = self._search(val)
        if found_node.val == val:
            return found_node

    def delete(self, val):
        found_node = self._search(val)
        if found_node.val == val:
            found_node.prev.next = found_node.next
            found_node.next.prev = found_node.prev
        self.size -= 1
