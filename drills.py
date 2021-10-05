"""
Given the head of a listNode, and a value,
remove every node in that linked list, that has the value

return the head

Input:  1->2->6->3->4->5->6->None, val = 6
Output: 1->2->3->4->5

6->5->-6-7, 6


traverse the linked
delete:
    1. previous node's .next and pointing it to the .next of the node being deleted


"""


"""
1->2->3->4->5->6, val = 6
[1->, 2->, 3->, 4]
Var           Value
head          1->
value          6
                0   1     2   3    4
queue         [1->, 2->, 3->, 4->, 5->]
node           5->
prev_node      4->
i              4

current initially head

"""


class ListNode(object):
    def __init__(self, val):
        """Initialize this node with the given data."""
        self.val = val
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return "Node({!r})".format(self.val)


def remove(head, val):
    """Time Complexity - O(n), Space - O(n - d)"""
    # init a queue - O(1)
    queue = list()
    # traversal of all the listnode -  O(n)
    node = head
    while node is not None:  # n iterations
        # only enqueue the nodes not being "deleted"
        if node.val != val:
            queue.append(node)
        node = node.next
    # modify all the next pointers in the queue
    for i in range(1, len(queue)):  # n - d
        prev_node, node = queue[i - 1], queue[i]
        prev_node.next = node
    # delete the tail if it's value matches the target value  - O(1)
    tail = queue[-1]
    if tail.next.val == val:
        queue[-1].next = None
    # update the head node if necessary
    if head.val != queue[0].val:
        head = queue[0]
    return head


# n + n --> O(n)

"""
if __name__ == '__main__':
    # Input:  1->2->6->3->4->5->6->None, val = 6
    node = ListNode(6)
    node.next = ListNode(2)
    node.next.next = ListNode(6)
    node.next.next.next = ListNode(3)
    node.next.next.next.next = ListNode(4)
    node.next.next.next.next.next = ListNode(5)
    node.next.next.next.next.next.next = ListNode(6)

    new_node = remove(node, 6)
    while new_node is not None:
        print(new_node)
        new_node = new_node.next
"""

"""August 14, 2020"""
