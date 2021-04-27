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
    1) init --> 
        input: head: DoublyLinkedNode, 
        tail: DoublyLinkedNode; 
        output: None
    2) add_node ---> input: "prepend"; output: None
    3) remove_node --> passes in a node: WATCH OUT for pointers
    4) move_to_front: passes in a node
    5) pop_tail --> removes the tail 

    """
    def __init__(self):
        # using DUMMY NODES
        self.head, self.tail = DoublyLinkedList(None, "head"), DoublyLinkedList(None, "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        # init size to NOT include the dummy nodes
        self.size = 0


    def add_node(self, node):
        '''adds node the front'''
        # connect the node to its related nodes in the list
        node.prev = self.head
        node.next = self.head.next
        # watch the order - insert the node into the list
        self.head.next.prev = node
        self.head.next = node
        # increase the size
        self.size += 1

    def remove_node(self, node):
        '''ASSUME the node is in the list'''
        # adjust pointers
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        # increase the size
        self.size -= 1

    def pop_tail(self):
        '''ASSUME the head and tail are not None'''
        self.remove_node(self.tail)

    def move_to_front(self, node):
        '''ASSUME the node is in the list'''
        self.remove_node(node)
        self.add_node(node)

    def __str__(self):
        items = list()

        node = self.head.next

        while node != self.tail:
            items.append(node.value)

        print(f"DLL: {items}")


class LRUCache:
    """
    Composition of DLL + hashmap

    DLL - quick access to items, large memory cap
    HM - maps the key to the node objects
    """
    def __init__(self, capacity) -> None:
        # client defines the limit for # items in the cache
        self.cap = capacity
        # instantiate the required objects
        self.lookup_table = dict()
        self.items = DoublyLinkedList()

    def get(self, key):
        requested_value = -1  # return -1 if key is not in the cache
        if key in self.lookup_table:
            # lookup the node in the table
            node = self.lookup_table[key]
            # move the node to the front of the list
            self.items.move_to_front(node)
            requested_value = node.value
        # return the value of the node
        return requested_value

    def put(self, key, value):
        # make a new DLL node
        node = DoublyLinkedList(key, value)
        # remove the tail (from the table and list) if cap is already reached
        if self.items.size == self.cap:
            del self.lookup_table[self.items.tail.key]
            self.items.pop_tail()
        # map key -> node
        self.lookup_table[key] = node
        # add node to the list
        self.items.add_node(node)
