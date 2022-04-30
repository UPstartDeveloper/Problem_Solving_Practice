from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    BASE = 10

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Input:
            2 immutable, non-empty, int LL
               
        Intuition
            pointers
            decoding/encoding
            
        Link: https://leetcode.com/problems/add-two-numbers/
        """
        ### HELPERS
        def _encode(value):
            # special case:
            if value == 0:
                return ListNode(0)
            # A: head pter = None
            head, node = None, None
            # B: calculate pow = 10
            # C: making a new list
            while value:
                # modulo div of val % pow
                digit = value % self.BASE
                # update the value ---> // pow
                value = value // self.BASE  # //=?
                # add a new ListNode obj  (set head node as appropiate)
                if head is None:
                    head = node = ListNode(digit)
                else:
                    node.next = ListNode(digit)
                    node = node.next
            return head

        def _decode(head):
            """given a SLL ---> give the int equivalent"""
            # A: determine length
            length, node = 0, head
            while node is not None:
                length += 1
                node = node.next
            # B: convert to a int (2nd traversal)
            total, node, pos = 0, head, 0
            while node is not None:
                # acculmulate this value
                exp10 = length - pos - 1
                total += node.val * (self.BASE ** exp10)
                # move on
                node = node.next
                pos += 1
            # C: return the total value of this LL
            return total

        def _reverse(head):
            """reverse a SLL in O(n), O(1) space"""
            prev, curr = None, head
            while curr is not None:
                # reverse 1st edge curr->successor
                successor = s = curr.next
                curr.next = prev
                # move pointers fwd
                prev = curr
                curr = s
            return prev

        ### MAIN
        # A: decode both lists ---> base 10 ints
        values = [_decode(head) for head in [l1, l2]]
        # B: sum
        total = sum(values)
        # C: encode as a SLL
        l3 = _reverse(_encode(total))
        # D: return the output
        return l3
