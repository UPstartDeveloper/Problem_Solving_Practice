class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def delete(self, prev, node):
        # "delete" the node that's a dupe
        prev.next = node.next
        # move the iterator node ahead from the deleted node's place
        node = prev.next
        return prev, node

    def __str__(self):
        items = list()
        n = self.head
        while n is not None:
            items.append(n.data)
            n = n.next
        return str(items)

    def remove_duplicates(self):
        '''Linear time and space'''
        # init a set
        unique_elems = set()
        # iterate over the list
        prev, node = None, self.head
        while node is not None:
            # check if this Node is a duplicate
            if node.data in unique_elems:
                # delete the node from the list
                prev, node = self.delete(prev, node)
            else:  # node does not have a duplicate value
                # add the value to the set
                unique_elems.add(node.data)
                # move both nodes ahead
                prev = node
                node = node.next
        return self.head


if __name__ == "__main__":
    # 1 --> -1 --> 6 --> 5 --> 7 -->
    """
    unique = {1, -1, 6, 5, 7}
    p = 7
    n = None
    """
    # Test Case 1:
    items = [1, -1, 6, 5, 1, 5, 7]
    # form the list
    head = Node(items[0])
    ll = LinkedList(head)
    node = ll.head
    for index in range(1, len(items)):
        new_node = Node(items[index])
        node.next = new_node
        node = new_node
    # test the output of the function
    ll.remove_duplicates()
    print(f'Items: {ll}')
