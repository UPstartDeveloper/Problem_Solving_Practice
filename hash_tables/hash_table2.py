class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head, self.tail = None, None

    def add(self, new_node: ListNode, append=True):
        ### HELPERS
        def _append(new_node):
            if self.head is None:  # add both head and tail
                self.head = new_node
                self.tail = new_node
            elif self.head == self.tail:
                self.head.next = self.tail
            self.tail.next = new_node
            self.tail = new_node

        def _prepend(new_node):
            if self.head is None:  # no prev nodes
                self.head, self.tail = new_node, new_node
            else:
                new_node.next = self.head
                self.head = new_node

        ### MAIN
        if append is True:
            _append(new_node)
        else:
            _prepend(new_node)

    def _find(self, val):
        prev, node = None, self.head
        while node is not None and node.val != val:
            prev = node
            node = node.next
        return prev, node

    def search(self, val):
        _, node = self._find(val)
        return node

    def items(self):
        """return a list of the values of all nodes in this list"""
        values, node = list(), self.head
        while node is not None:
            values.append(node.val)
            node = node.next
        return values

    def delete(self, val):
        prev, node = self._find(val)
        if node is not None:
            if node == self.head:  # and prev is None
                self.head = self.head.next
                return
            elif node == self.tail:
                self.tail = prev
            prev.next = node.next


class HashTable:
    def __init__(self, num_buckets=8):
        """uses separate chaining"""
        self.buckets = [LinkedList() for _ in range(num_buckets)]

    def _get_bucket(self, key):
        bucket_index = hash(key) % len(self.buckets)
        return self.buckets[bucket_index]

    def put(self, key, value):
        bucket = self._get_bucket(key)
        pair = bucket.search((key, value))
        if pair is not None:  # update a ListNode
            pair.val = (key, value)
        else:  # add a ListNode
            bucket.add(ListNode(val=(key, value)))

    def get(self, key):
        bucket = self._get_bucket(key)
        # Linear Search
        pairs = bucket.items()
        for item_key, item_val in pairs:
            if key == item_key:
                return item_val
        else:
            return None

    def remove(self, key):
        # verify the key-value pair in this bucket
        value = self.get(key)
        if value is not None:
            bucket = self._get_bucket(key)
            bucket.delete((key, value))
