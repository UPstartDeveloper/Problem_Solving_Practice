import string

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
        """Deletes the first node that has the matching value."""
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
        """Inserts a new node n steps into the list, if possible."""
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
                print(
                    f"List of size {self.size()} is too \
                        small to insert at {steps} steps."
                )
        else:  # err msg for new_node
            print(
                f"Cannot insert new_node of type {type(new_node)}.\
                    Pass a ListNode instead."
            )

    def update(self, current_val, new_val):
        """Replaces the value in the first node with current_val."""
        node = self.head
        while node is not None:
            # replace node val
            if node.val == current_val:
                node.val = new_val
            # regardless, move ahead
            node = node.next

    def search(self, node_val):
        """Returns the node if found having node_val"""
        node = self.head
        while node is not None:
            if node.val == node_val:
                return node
            node = node.next
        return None

    def search_key(self, node_key):
        """Returns the value if a node has the node_key in its tuple.
        HashTable-specific (see HashTable.get below).
        """
        node = self.head
        while node is not None:
            key, value = node.val
            if node_key == key:
                return value
            node = node.next
        # if not found, return None
        return None

    def items(self):
        """returns a list of the values of each node in the list."""
        values = list()
        node = self.head
        while node is not None:
            values.append(node.val)
            node = node.next
        return values


"""Hash Table Class"""


class HashTable:

    LOAD_FACTOR_THRESHOLD = 0.5
    # HASH_FUNC_UPPER_BOUND = 10_000_000_000

    def __init__(self, num_buckets=8):
        """A resizable hash table that uses
        a dynamic array w/ separate chaining.

        Remember that keys in a HashTable must be unique!
        """
        self.buckets = [LinkedList() for _ in range(num_buckets)]
        self.num_entries = 0

    def _hash(self, key):
        hash_value = hash(key)  # a unique hash for each unique key
        bucket_index = hash_value % len(self.buckets)
        return bucket_index

    def _resize_buckets(self):
        # find the current load factor
        load_factor = self.num_entries / len(self.buckets)
        # check if we need to resize
        if load_factor > self.LOAD_FACTOR_THRESHOLD:
            # print('resizing')
            # dump out all the entries into another list
            entries = self.items()
            # make the bucket array triple in size
            self.buckets = [LinkedList() for _ in range(len(self.buckets) * 3)]
            # readd all the entries into the new buckets array
            self.num_entries = 0
            for key, value in entries:
                self.set(key, value)
        # else:
        #     print('not resizing')

    def set(self, key, value):
        """Add or update entries in the hash table."""
        # A: find the bucket index where the entry belong
        bucket_index = self._hash(key)
        # B: go to that chain in the bucket array
        chain = self.buckets[bucket_index]
        # C: if found - get the item, then replace it
        new_val = (key, value)
        searched_value = chain.search_key(key)
        if searched_value is not None:
            current_val = (key, searched_value)
            chain.update(current_val, new_val)
        # D: If adding, resize afterwards if needed.
        else:  # the key was not in the chain already
            chain.append(ListNode(new_val))
            self.num_entries += 1
            self._resize_buckets()

    def items(self):
        """get a list of all the key-value pairs"""
        entries = list()
        for chain in self.buckets:
            entries.extend(chain.items())
        return entries

    def unset(self, key):
        """remove a key-value pair"""
        bucket_index = self._hash(key)
        chain = self.buckets[bucket_index]
        value = self.get(key)
        chain.delete((key, value))

    def get(self, key):
        """return the value associated with a given key"""
        # hash the key
        bucket_index = self._hash(key)
        value = self.buckets[bucket_index].search_key(key)
        return value


if __name__ == "__main__":
    letters = list(string.ascii_letters)
    numbers = list(range(26))
    # init HashTable
    ht = HashTable()
    # add all the letters and numbers to the HashTable
    for i in range(26):
        key = letters[i]
        value = numbers[i]
        ht.set(key, value)
    # see if we can get all the items back - check if it's unordered
    print(ht.items())
    # see the distribution of bucket sizes
    ht_size = 0
    for chain in ht.buckets:
        print(chain.size())
        ht_size += chain.size()
    # check that the size is calculated correctly
    print(ht.num_entries, ht_size)
