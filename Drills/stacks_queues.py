class ArrayStack:
    def __init__(self, elems) -> None:
        self.items = elems

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def top(self):
        if len(self.items) > 0:
            return self.items[-1]


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head, self.tail = head, tail
        self.size = 0

    def add(self, new_node, prepend=False):
        ### HELPERS
        def _prepend(new_node):
            if self.head is None:  # no nodes yet
                self.head = self.tail = new_node
            else:  # self.head is not None
                new_node.next = self.head
                self.head = new_node

        def _append(new_node):
            if self.tail is None:  # no nodes net
                self.head = self.tail = new_node
            else:  # self.tail is not None
                self.tail.next = new_node
                self.tail = new_node

        ### DRIVER
        if prepend is True:
            _prepend(new_node)
        else:
            _append(new_node)
        self.size += 1

    def _find(self, value):
        prev, node = None, self.head
        while node and node.val != value:
            prev = node
            node = node.next
        return prev, node

    def search(self, node_val):
        _, found = self._find(node_val)
        if found is not None:  # a ListNode obj
            return found

    def delete(self, value):
        prev, found = self._find(value)
        if found is not None:
            # deleting head - move the head fwd
            if self.head == found:
                self.head = self.head.next
            # deleting mid - move prev "around" the node to delete
            if prev is not None:
                prev.next = found.next
            # deleting tail - added step, reset tail point
            if self.tail == found:
                self.tail = prev
            # all cases - decrement the size
            self.size -= 1
            # all done!
            return found


class LinkedStack:
    def __init__(self):
        self.items = LinkedList()

    def push(self, item_val):
        item = ListNode(item_val)
        self.items.add(item, prepend=True)

    def pop(self):
        if self.items.size > 0:
            top_val = self.items.head.val
            _ = self.items.delete(top_val)
            return top_val

    def top(self):
        if self.items.size > 0:
            return self.items.head.val


class LinkedQueue:
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, new_val):
        new_node = ListNode(new_val)
        self.items.add(new_node)

    def front(self):
        if self.items.size > 0:
            return self.items.head.val

    def dequeue(self):
        if self.items.size > 0:
            front_val = self.items.head.val
            _ = self.items.delete(front_val)
            return front_val


if __name__ == "__main__":
    ll = LinkedList()
    nodes = [ListNode("A"), ListNode("B"), ListNode("C"), ListNode("D")]
    assert ll.head == None
    assert ll.tail == None
    ll.add(nodes[0])
    assert ll.size == 1
    assert ll.head == ll.tail == nodes[0]
    assert ll.head.next == ll.tail.next == None
    ll.add(nodes[1])
    assert ll.size == 2
    assert ll.head.next == ll.tail
    assert ll.head.next == nodes[1]
    ll.delete("B")
