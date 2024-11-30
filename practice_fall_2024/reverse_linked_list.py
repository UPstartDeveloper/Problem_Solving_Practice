from typing import Optional


class ListNode:
    """Definition for singly-linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """https://neetcode.io/problems/reverse-a-linked-list"""
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Input(s):
            head:
                null or ListNode
                may or may not have a next pointer

        Output(s):
            modified head of the list

        EC:
            head is null - return head
            head is alone - no change
            invalid node vals - N/A

        Intutions:
            BCR is linear, perhaps constant space

        Approaches:

            1) Naive - utilize a Stack
                O(n) time + space

                A: traverse forward
                    - push all nodes onto a stack
                    - save the last node as the future_head

                B: traverse backwards
                    - pop nodes off the stack - use this to reverse the pointers

                C: return future_head

            2) Two (or Three?) pointers?
                O(n) time, O(1) space

             <- 0 <- 1 <- 2 <- 3
                          n
                               p c
                pters
                    prev    = p
                    current = c

                Subproblem:
                    inputs: p, c
                    algo:
                        while c:
                            set next = n = c.next
                            set c.next = p
                            set p = c
                            set c = next
                    return: p
        """
        ### HELPER(S)
        ...

        ### DRIVER:

        # A: check EC
        if not head or not head.next:
            return head

        # B: run main algo
        prev = p = None
        current = c = head

        while c:
            # set next = n = c.next
            next_node = c.next
            # set c.next = p
            c.next = p
            # set p = c
            p = c
            # set c = next
            c = next_node
        return p
