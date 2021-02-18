class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def print_items(self):
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next

    def append(self, new_node: ListNode):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def prepend(self, new_head: ListNode):
        new_head.next = self.head
        self.head = new_head

    def _traverse(n_steps):
        node = self.head
        prev = None
        for _ in range(n_steps):
            prev = node
            node = node.next
        return prev, node

    def insert(self, new_node, n_steps):
        node_before, current_node = self._traverse(n_steps)
        if node_before is not None:
            node_before.next = new_node
            new_node.next = current_node
        else:  # we're doing a prepend operation
            self.prepend(new_node)

    def update(self, new_val, n_steps):
        node_before, current_node = self._traverse(n_steps)
        current_node.val = new_val

    def delete(self, n_steps):
        node_before, deleting_node = self._traverse(n_steps)
        if node_before is not None and deleting_node is not None:
            node_before.next = deleting_node.next
        elif node_before is None:
            self.head = deleting_node.next
