class DoublyLinkedNode:
    '''stores a key, value, prev, and next - key is probably unique'''
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """
    Attributes:
    head: DoublyLinkedNode
    tail: DoublyLinkedNode
    size

    Methods:
    1) init --> input: head: DoublyLinkedNode, tail: DoublyLinkedNode; output: None
    2) add_node ---> input: "prepend"; output: None
    3) remove_node --> passes in a node: WATCH OUT for pointers
    4) move_to_front: passes in a node
    5) pop_tail --> removes the tail 

    """
    def __init__(self, head=None, tail=None):
        self.head, self.tail = head, tail
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        if self.head:
            self.size += 1
        
        if self.tail:
            self.size += 1

    def add_node(self, node):
        '''input: "prepend"; output: None'''
        if self.head is not None:
            self.head.prev = node
        old_head = self.head
        self.head = node
        self.head.next = old_head.next

    def remove_node(self, node):
        '''remove the node, and return it'''
        deleted = self.head

        while deleted is not None:
            # node found
            if deleted.value == node.value:
                # deleting the head
                if deleted == self.head:
                    old_head = self.head
                    self.head = old_head.next
                    self.head.prev = old_head.prev
                else:  # not deleting the head
                    deleted.prev.next = deleted.next
                    deleted.next.prev = deleted.prev
                # return the deleted node
                return deleted
            # node not found
            deleted = deleted.next

    def pop_tail(self):
        old_tail = self.tail
        old_tail.prev.next = old_tail.next
        self.tail = old_tail.prev
        return old_tail

    def move_to_front(self, node):
        node = self.remove_node(node)
        self.add_node(node)
