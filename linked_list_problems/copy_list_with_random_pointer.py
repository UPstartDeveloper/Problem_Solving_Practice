from typing import Optional


class Node:
    """Definition for a Node."""

    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """LeetCode: https://leetcode.com/problems/copy-list-with-random-pointer/"""

        ### HELPERS

        def _clone(node):
            if node is not None:
                return Node(x=node.val)
            return None

        def _copy_sll_deep(head):
            """copy only the values for now"""
            clone_head = ch = _clone(head)
            orig_clones = dict()
            # traverse w/ 2 pters
            clone_node, node = ch, head
            while node is not None:
                # get the next node into the cloned list
                clone_node.next = _clone(node.next)
                # map original --> its clone
                key = (node,)
                orig_clones[key] = clone_node
                node, clone_node = node.next, clone_node.next
            return clone_head, orig_clones

        def _map(head, clone_head):
            clone_node, node = clone_head, head
            orig_clones = dict()
            while node is not None:
                # map original --> its clone
                key = (node,)
                orig_clones[key] = clone_node
                # move on
                node, clone_node = node.next, clone_node.next
            return orig_clones

        ### MAIN
        # A: init clone SLL
        clone_head, orig_clones = _copy_sll_deep(head)
        # B: traverse - add in .random
        clone_node, node = clone_head, head
        while node is not None:
            random_pter = node.random
            # connect corr. to clone
            if random_pter is not None:
                clone_node.random = orig_clones[(random_pter,)]
            # move on
            node, clone_node = node.next, clone_node.next

        return clone_head
