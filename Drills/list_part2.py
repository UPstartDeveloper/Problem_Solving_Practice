class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

        if self.head is not None:
            self.size = 1
        if self.tail is not None:
            self.head.next = self.tail
            self.size = 2
        elif tail is None:
            self.tail = self.head

    def _find_prev_and_node(self, val):
        prev, node = None, self.head

        while node is not None and node.val != val:
            prev = node
            node = node.next

        # found
        if node is not None:
            return prev, node
        # not found
        return prev, -1

    def find(self, value):
        prev, node = self._find_prev_and_node(value)
        # found
        if node is not None:
            return node
        # not found
        return -1

    def append(self, value):
        if self.head is None:
            self.prepend(value)
        else:
            # adding the node
            new_node = ListNode(value)
            if self.tail is None:
                self.head.next = new_node
            else:
                self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def prepend(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        if self.head is None:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def update(self, current_val, new_val):
        """
        what to return if not found?
        SLL or DLL?
        what properties to have?
        are the values unique?
        """
        # find the node
        prev, node = self.__find_prev_and_node(current_val)
        # if found, update it
        if node != -1:
            node.val = new_val

    def delete(self, value):
        # find the node
        prev, node = self._find_prev_and_node(value)
        # if node is the head, move the head
        # TODO: handle not found
        if node == -1:
            return
        # deleting the head node
        elif node == self.head:
            self.head = self.head.next
        # otherwise move the prev.next pointer around the node
        elif prev is not None:
            prev.next = node.next
        # modify tail pter if needed
        if node == self.tail:
            self.tail = prev
        # update size
        self.size -= 1
        return node


class LinkedQueue:
    def __init__(self):
        self.q = LinkedList()

    def front(self):
        if self.q.size > 0:
            return self.q.head.val

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        if self.q.size > 0:
            head_val = self.front()
            self.delete(head_val)
            return head_val
