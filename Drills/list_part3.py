class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"Node {self.val}"


class LinkedList:

    def __init__(self, head, tail=None):
        self.head = head
        self.tail = self.head
        if tail is not None:
            self.tail = tail
            self.head.next = self.tail

    def append(self, new_val):
        new = ListNode(new_val)
        if self.tail is not None:
            self.tail.next = new
        else:
            self.head = new
        self.tail = new

    def get_node(self, node_val):
        '''ASSUMES the node in list'''
        prev, node = self._get_node(node_val)
        return node

    def update_node(self, current_val, new_val):
        '''ASSUMES the node in list'''
        prev, node = self._get_node(current_val)
        node.val = new_val
        
    def _get_node(self, node_val):
        prev, node = None, self.head
        while node is not None and node.val != node_val:
            prev = node
            node = node.next
        return prev, node

    def delete(self, deletion_val):
        # A: linear search for the node_val
        prev, node = self._get_node(deletion_val)
        # E: if not found, raise error
        if node is None:
            raise ValueError(f"node w/ {deletion_val} not in this list")
        # B: node being deleted is the head
        elif node == self.head:
            # change the head
            self.head = self.head.next
        # C: otherwise, delete by "skipping the node"
        else:  
            prev.next = node.next
            # D: if deleted node is tail, move tail
            if node == self.tail:
                self.tail = prev
    
    def prepend(self, new_val):
        node = ListNode(new_val)
        node.next = self.head
        self.head = node
