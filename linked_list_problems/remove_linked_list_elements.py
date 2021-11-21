from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Leetcode: https://leetcode.com/problems/remove-linked-list-elements/

        Input/Problem:
            SLL
            int
            mutating the SLL
            mutable

        Intuition:
            pointers

            Stepping Stone
                delete one node
                multiple times

        EC:
            1) val nto found ---> !modify
            2) null head = return None
            3) head is deleted ---> head = head.next
            4) node.val or val ---> ValueError
            5) mmultiple nodes to del, w/ node.val

        Approach:

            1) Brute force - array
                linear time and space

            2) Multiple passes
                - delete_one_value
                - call it until it doesn't make any changes
                - const space, O(k * n), k = # of nodes to delete

            3) 1 pass, constant space

            A: init prev = None, node = head
            B: delete all in one pass
            while node is not None:
                # check if node.val === val -- decide IF delete
                    # check if head or not ---> decide HOW to delete
                # move both pointers fwd
                parent = node
                node = node.next
            C: return new head


            [1,2,6 --> None], val = 6
                 p   n

        """
        # A: init prev = None, node = head
        prev, node = None, head
        # B: delete all in one pass
        while node is not None:
            # a. decide IF to delete
            if node.val == val:
                # 1) move to the end of (possible) repeated sequence
                while node.next and node.next.val == val:
                    node = node.next
                # 2) decide HOW to delete
                if head.val == val:  # if the head is in the sequence being deleted
                    head = node.next
                elif prev is not None:  # deleting a sequence in the middle/end
                    prev.next = node.next
            # b. move both pointers fwd
            prev = node
            node = node.next
        # C: return new head
        return head


"""
Conceptual Test:
    [1 -> 2 --- -> 3 -> 6 -> None val = 6
               6
                   p    n

    [1 -> 2 -> 6 -> 6 -> None val = 6
          p.        n
          
    7 -> 7 -> 7 -> 7 ->
p.                 n

"""
