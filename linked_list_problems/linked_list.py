class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None


class LinkedList:
    def __init__(self, head=None, items=None):
        self.head = head  # ListNode

        if items is not None:  # should be List[ListNode]
            for node in items:
                self.append(node)

    def append(self, node):
        # adding a head
        if self.head is None:
            self.head = node
        else:
            # add a node after the head
            prev, current_node = None, self.head
            while current_node is not None:
                prev = current_node
                current_node = current_node.next

            prev.next = node
    
    def prepend(self, node):
        node.next = self.head
        self.head = node

    def delete(self, node_val):
        '''Deletes the first node that has the matching value.'''
        # find the node with the value
        prev, current_node = None, self.head
        while current_node.val != node_val:
            prev = current_node
            current_node = current_node.next
        # if it's not the head, then set the .next of the previous node
        if self.head != current_node:
            prev.next = current_node.next
        # if it is the head, move down the head pointer
        elif self.head == current_node and self.head is not None:  
            self.head = self.head.next

    def size(self):
        length = 0
        node = self.head 
        while node is not None:
            node = node.next
            length += 1
        return length

    def get_tail(self):
        prev, node = None, self.head
        while node is not None:
            prev = node
            node = node.next

        return prev

    def insert(self, steps, new_node):
        '''Inserts a new node after n steps into the list, if possible.'''
        if steps <= self.size():
            current_node = self.head
            steps_taken = 0
            while steps_taken < steps:
                current_node = current_node.next
                steps_taken += 1
            next_node = current_node.next
            current_node.next = new_node
            new_node.next = next_node
    