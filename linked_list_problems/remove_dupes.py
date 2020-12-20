class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def delete(prev, node):
        prev.next = node.next

    def __str__(self):
        pass

    def remove_duplicates(self):
        # init a set
        unique_elems = set()
        # iterate over the list
        prev, node = None, self.head
        while node is not None:
            # check if this Node is a duplicate
            if node.data in unique_elems:
                # delete the node from the list
                self.delete(prev, node)
            else:  # node does not have a duplicate value
                # move both nodes ahead
                prev = node
                node = node.next
        return self.head


if __name__ == "__main__":
    pass