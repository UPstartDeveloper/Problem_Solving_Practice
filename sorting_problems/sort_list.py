from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode: m"""
        ### HELPERS
        def _print_list(head):
            '''use to help debugging'''
            nodes = list()
            node = head
            while node:
                nodes.append(node.val)
                node = node.next
            print(nodes, head)
            return 
        
        ### DRIVER - iterative bubble sort - O(n**2) time, O(1) space
        is_sorted = False
        dummy_node = ListNode(None, next=head)
        # begin sorting
        while is_sorted is False:
            swaps = 0
            node1 = head 
            dummy_node.next = head
            prev = dummy_node
            # one pass over list
            while node1 is not None:
                node2 = node1.next
                needs_swap = node2 and (node2.val < node1.val)
                if needs_swap is True:
                    # swap
                    node1.next = node2.next
                    node2.next = node1
                    node1, node2 = node2, node1  # simplifies pointer updates
                    # update the head if this is the start of the list
                    if prev == dummy_node:
                        head = node1
                    prev.next = node1
                    swaps += 1
                # move forward
                prev = prev.next
                node1 = node1.next
            # still swap?
            if swaps == 0:
                is_sorted = True
        return head
