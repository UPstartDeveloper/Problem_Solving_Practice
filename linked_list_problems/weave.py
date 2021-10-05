"""
Using "The Runner Technique"

For example, suppose you had a linked list
a1 -> a2 -> ••• -> an -> b1 -> b2 -> ••• -> bn

and you wanted to rearrange it into

a1 -> b1 -> a2 -> b2 -> •••

You do not know the length of the linked list 
(but you do know that the length is an even number).

"""

from typing import Tuple


class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head: ListNode) -> None:
        self.head = head


class Solution:
    def find_midpoint(self, list: LinkedList) -> Tuple[ListNode]:
        p1, p2 = list.head, list.head.next
        # move p1 to the rough midpoint of the list, and p2 to the end
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next

        return p1, p2

    def weave(self, start: ListNode, midpoint: ListNode) -> None:
        """insert elements from after the midpoint node, to after the starting node"""
        while midpoint.next.next is not None:
            # A: save a pointer for the node after the midpoint-starting node
            temp = midpoint.next
            # B: update the node after the midpoint-starting node
            midpoint.next = temp.next
            # C: update the node after the starting node
            temp.next = start.next
            start.next = temp
            # D: move the starting pointer ahead
            start = start.next.next

    def rearrange(self, list: LinkedList) -> LinkedList:
        # A: find the midpoint of the list
        midpoint, end = self.find_midpoint(list)
        # B: set a third pointer at the head of the list
        start = list.head
        # C: weave the list into the order described above (alt. a and b)
        self.weave(start, midpoint)
        # D: return the modified list
        return list
