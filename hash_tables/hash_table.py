"""Linked List used for Separate Chaining"""
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
        if self.head != current_node:  # current_node is the node to delete
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

    def insert(self, new_node, steps):
        '''Inserts a new node n steps into the list, if possible.'''
        # validate the input
        if isinstance(new_node, ListNode):
            if steps <= self.size(): 
                # find the node exactly at n steps into the list  
                prev, current_node = None, self.head
                steps_taken = 0
                while steps_taken < steps:
                    prev = current_node
                    current_node = current_node.next
                    steps_taken += 1
                # check if we are doing a prepend
                if prev is None:
                    self.prepend(new_node)
                # otherwise move the new node into place
                prev.next = new_node
                new_node.next = current_node
            # check if we are doing an append op
            elif steps == self.size() + 1:
                self.append(new_node)
            else:  # err msg for steps 
                print(f"List of size {self.size()} is too \
                        small to insert at {steps} steps.")
        else:  # err msg for new_node
            print(f"Cannot insert new_node of type {type(new_node)}.\
                    Pass a ListNode instead.")


"""Hash Table Class"""
import random


class HashTable:

    LOAD_FACTOR_THRESHOLD = 0.5
    HASH_FUNC_UPPER_BOUND = 10_000_000_000

    def __init__(self, num_buckets=8):
        """A resizable hash table that uses 
        a dynamic array w/ separate chaining.
        
        Remember that keys in a HashTable must be unique!
        """
        self.buckets = [
            LinkedList() for _ in range(num_buckets)
        ]

    def _hash(self):
        hash_value = random.randint(self.HASH_FUNC_UPPER_BOUND)
        bucket_index = hash_value % len(self.buckets)
        return bucket_index

    def _resize_buckets(self):
        # find the current load factor
        total_entries = sum([chain.length() for chain in self.buckets])
        load_factor = total_entries / len(self.buckets)
        # check if we need to resize
        if load_factor > self.LOAD_FACTOR_THRESHOLD:
            # dump out all the entries into another list
            entries = self.items()
            # make the bucket array triple in size
            self.buckets = [
                LinkedList() for _ in range(len(self.buckets) * 3)
            ]
            # readd all the entries into the new buckets array
            for key, value in entries:
                self.set(key, value)

    def set(self, key, value):
        # TODO: add or update entries. If adding, resize afterwards if needed.
        pass

    def items(self):
        # TODO: get a list of all the key-value pairs
        pass

    def unset(self, key):
        # TODO: remove a key-value pair
        pass

    def get(self, key):
        # TODO: return the value associated with a given key
        pass