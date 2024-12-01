# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """https://neetcode.io/problems/reorder-linked-list"""
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Input(s):
            head of a non-empty SLL

        Output(s):
            same head, modified SLL
            no changes to vals, only the next ptrs

        EC + Assumptions:
            1 node --> return it as is

        Intuitions:

            BCR -
                time: O(n)
                space: O(1)??

            goal: interlace the reverse of the
                    second half of the list, with the first

        Approaches:
                  v
        [0, 1, 2, 3, 4, 5, 6]

        [0, 1, 2,
                  ^

        [6, 5, 4, 3]
                  ^

         [0, 6, 1, 5, 2, 4]
        count = 7
        mid =

            1) use of pointers?

                A: traverse the list once - count # of nodes

                B: locate the middle node

                C: use 2 ptrs - break off + reverse the 2nd half

                D: using 3-4 ptrs, interlace the lists

                    current_node1 = head1
                    current_node2 = head2

                    while current_node1 and current_node2:
                        temp1 = current_node1.next
                        temp2 = current_node2.next

                        current_node1.next = current_node2

                        if temp1:
                            current_node1.next.next = temp1

                        current_node1 = temp1
                        current_node2 = temp2

        """
        ### HELPER(S)
        def _count_num_nodes(node):
            """works :)

            [0, 1, 2, 3, 4, 5, 6]
                                  n

             count = 0, 1, 2, 3, 4, 5, 6, 7
            """
            count = 0

            while node:
                count += 1
                node = node.next

            return count

        def _find_mid(num_nodes):
            """works (I think )

            [0, 1, 2, 3, 4, 5, 6]
                      n

             7 // 2 = 3
            """
            prev = None
            node = head

            for _ in range(num_nodes // 2):
                prev = node
                node = node.next

            return node

        def _reverse_second_half(mid):
            """ works :)

           <- 3 <- 4 <- 5 <- 6
            p  n   t
              p   n.   t
                   p.  n.  t
                            p.  n.  t
            """
            prev, node = None, mid

            while node:
                print(f"prev: {prev.val if prev else None}")
                print(f"node: {node.val}")
                temp = node.next
                node.next = prev
                prev = node
                node = temp

            return prev

        def _merge_and_reorder(head1, head2):
            """TODO[test]"""
            current_node1 = head1
            current_node2 = head2
            while current_node1 and current_node2:
                temp1 = current_node1.next
                temp2 = current_node2.next

                if temp1 == current_node2 or temp2 == current_node1:
                    return

                current_node1.next = current_node2
                current_node1.next.next = temp1
                current_node1 = temp1
                current_node2 = temp2

            return head1

        ### DRIVER
        # EC:
        if not head.next:
            return

        # A: traverse the list once - count # of nodes
        num_nodes = _count_num_nodes(head)

        # B: locate the middle node
        mid = _find_mid(num_nodes)

        # C: use 2 ptrs - break off + reverse the 2nd half
        head1 = head
        head2 = _reverse_second_half(mid)

        # D: using 3-4 ptrs, interlace the lists
        _merge_and_reorder(head1, head2)
