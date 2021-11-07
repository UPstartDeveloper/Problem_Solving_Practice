# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detect_cycle(self, head: ListNode):
        """
        detect a cycle in a linked list, return the 0-index
            position of the repeated node

            - -1 if no cycle occurs

        are there duplicate elements in the linked list nodes?

        Assume:
            - there can not be duplicates
            - there will be at least one node in the list

        Stepping Stone Problems (help anchor my mind in the problem, what we need to do):
            - detecting a cycle in a linked list with NO Duplicates -
                keep track of items in a Python set(), and an index
                    - return the index if a duplicate appears, or -1
            - detecting a cycle in a linked list with duplicates
                    - find index of the tail - len(list) = tail_index + 1  - O(n)
                    - use two pointers - while loop O(n)
                        - 1 moves faster than the other
                        - if they overlap at any point, that determines if a cycle is found
                        - how to track the index?
                            - return the index of p1 % len(list)

                [3,2,0,-4]

                p1_index   |.   p2_index
                1               0
                3               1
                5               2
                7               3
                9               4

            what's the runtime of the while loop?
             n = 10,000 --> pretty long
            - detecting a cycle in a linked list with duplicates, constant space
        """
        # A: calculate the index of the tail
        node = head
        tail_index = -1
        node_items = set()
        while node.val not in node_items:
            node_items.add(node.val)
            node = node.next
            tail_index += 1
            print(f"Tail index: {tail_index}, set: {node_items}")
        LIST_LENGTH = tail_index + 1
        # B: init two pointers to traverse the list
        faster, slower = head.next, head
        faster_index, slower_index = 1, 0
        # C: see if the pointers overlap
        while faster is not None and faster.next is not None and faster != slower:
            # move the pointers up
            faster = faster.next.next
            slower = slower.next
            faster_index += 2
            slower_index += 1
            print(
                f"Faster: {faster_index, faster.val}, Slower: {slower_index, slower.val}"
            )
        # D: see if a cycle detected
        if faster == slower:
            return faster_index % LIST_LENGTH
        else:
            return -1

    """
    ll = [3,2,0,-4]
    node = None
    tail_index = 3
    LIST_LENGTH = 4
    
    slower | faster  | slower_index     | faster_index
      3        2            0                   1
      2       -4            1                   3
      0        0            2                   5
    """


if __name__ == "__main__":
    # set up the list
    nodes = [
        ListNode(3),
        ListNode(2),
        ListNode(0),
        ListNode(-4),
    ]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[1]
    # detect the cycle
    sol = Solution()
    print(sol.detect_cycle(nodes[0]))
