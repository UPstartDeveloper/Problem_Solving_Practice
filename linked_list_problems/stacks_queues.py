class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class DoublyNode(ListNode):
    def __init__(self, val):
        super().__init__(val)
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def _add_head(self, new_node: ListNode):
        self.head = self.tail = new_node

    def append(self, new_node: ListNode):
        if self.head is None:
            self._add_head(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node: ListNode):
        if self.head is None:
            self._add_head(new_node)
        else:
            new_node.next = self.head
            self.head = new_node

    def _find(self, target):
        """Linear search"""
        prev, node = None, self.head
        while node is not None and node.val != target:
            prev = node
            node = node.next
        return prev, node

    def search(self, target):
        prev, node = self._find(target)
        return node

    def delete(self, target):
        prev, node = self._find(target)
        if node is not None:
            if prev is None:
                self.head = self.head.next
            else:
                prev.next = node.next
                if node == self.tail:
                    self.tail = prev


class LinkedStack:
    """top is the head"""

    def __init__(self):
        self.items = LinkedList()

    def push(self, item: int):
        self.items.append(ListNode(item))

    def top(self) -> int:
        top_node = self.items.head
        if top_node is not None:
            return top_node.val
        return top_node

    def pop(self) -> ListNode:
        top_val = self.top()
        if top_val is None:
            return self.items.delete(top_val)
        return top_val


class LinkedQueue:
    """head is the front, tail is the back"""

    def __init__(self):
        self.items = LinkedList()

    def front(self) -> int:
        front_node = self.items.head
        if front_node is not None:
            return front_node.val
        return None

    def dequeue(self) -> ListNode:
        front_val = self.front()
        if front_val is None:
            return self.items.delete(front_val)
        return None

    def enqueue(self, new_item: int):
        self.items.append(ListNode(new_item))


class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyNode(None)
        self.tail = DoublyNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, new: DoublyNode) -> None:
        current_last = self.tail.prev
        current_last.next = new
        new.next = self.tail
        self.tail.prev = new

    def appendleft(self, new: DoublyNode) -> None:
        current_first = self.head.next
        new.prev = self.head
        new.next = current_first
        self.head.next = new

    def pop(self) -> int:
        last = self.tail.prev
        if last is not self.head:
            new_last = last.prev
            self.tail.prev = new_last
            new_last.next = self.tail
        return last.val

    def popleft(self) -> int:
        first = self.head.next
        if first is not self.tail:
            new_first = first.next
            new_first.prev = self.head
            self.head.next = new_first
        return first.val


class Deque(DoublyLinkedList):
    def front(self) -> int:
        if self.tail.prev == self.head:
            raise IndexError("There is no item at the front.")
        return self.tail.prev.val

    def back(self) -> int:
        if self.tail.prev == self.head:
            raise IndexError("There is no item at the back.")
        return self.head.next.val
