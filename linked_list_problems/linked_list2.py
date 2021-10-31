from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, items: List[int]):
        self.head, self.tail, self.size = None, None, 0
        for item in items:
            self.append(item)

    def append(self, item: int):
        new_node = ListNode(item)
        # no nodes in the list
        if self.head is None:
            self.head = self.tail = new_node
        # otherwise, if only 1 node so far
        else:
            # always add to the end of the list
            self.tail.next = new_node
            self.tail = new_node
        # increment size
        self.size += 1

    def prepend(self, item: int):
        new_node = ListNode(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def _find_node(self, val: int) -> ListNode:
        prev, current = None, self.head
        while current and current.val != val:
            prev = current
            current = current.next
        return prev, current

    def update(self, old_val, new_val):
        pass

    def delete(self, val) -> ListNode:
        prev, node = self._find_node(val)
        # update pointers
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = prev
        # node in the middle
        if prev is not None:
            prev.next = node.next
        # decrement size
        self.size -= 1


if __name__ == "__main__":
    items = [1, 2]
    ll = LinkedList(items)
