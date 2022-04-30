from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/"""

        ### HELPERS
        def _count_nodes(node):
            count = 1
            while node and node.next:
                if node.val == node.next.val:
                    count += 1
                    node = node.next
                else:
                    break
            return count

        def _is_unique(node):
            """assume node is non-null, and BEFORE any of its dupes"""
            return _count_nodes(node) == 1

        def _is_unique_and_count(node):
            count = _count_nodes(node)
            return count, count == 1

        def _next_unique(node):
            is_unique = False
            while node and is_unique is False:
                count, is_unique = _is_unique_and_count(node)
                # move ahead if not unique
                if is_unique is False:
                    for _ in range(count):
                        node = node.next
                # otherwise, break out of loop
                else:
                    is_unique = True
            return node

        ### MAIN
        if head is not None:
            # A: move head to the first "truly" unique node
            head = _next_unique(head)
            # B: delete any other dupes
            if head is not None:
                prev, node = head, head.next
                while node is not None:
                    # is it unique?
                    node = _next_unique(node)
                    # regardless - move prev (and del as appropiate)
                    prev.next = node
                    prev = prev.next
                    if node:
                        node = node.next
        return head
