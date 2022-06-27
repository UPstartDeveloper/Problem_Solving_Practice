from typing import Optional


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        LeetCode: https://leetcode.com/problems/merge-nodes-in-between-zeros/

        You are given the head of a linked list, 
        which contains a series of integers separated by 0's. 
        The beginning and end of the linked list will have Node.val == 0.
        
        For every two consecutive 0's, 
            merge all the nodes lying in between them into a single node 
            whose value is the sum of all the merged nodes. 
            
        The modified list should not contain any 0's.

        Return the head of the modified linked list.

        Example:
                          v
            in: [0, 3, 1, 0, 4, 5, 2, 0]
                 ^ 
                running = 3, 1   ---> 4
                [4, 3, 1, 0, 4, 5, 2, 0] 
                    ^                    ^
                running = 4, 9, 11

                [4, 11.next = None

                [4, 11]
                
                , 1, 0, 4, 5, 2, 0] 
            out:  [4, 11]

        Input:
            1 SLL - ints, mutable, pos/0, irregular, unsorted, dupes
            no 2 consecutive
            non-empty

        BCR:
            O(n) time
            O(1) space

        Output: new linked or modified

        EC:
            N/A
                empty list --> return right away
                consecutvies - iterate until they're skipped
                neg - not really a problem???

        Approach

        1) DIY

            A: init prev, further = head, head (aka the first "0")

            B: using further: traverse whole list
                find the next running sum
                stop at next zero

                C: set prev.val = running_sum

                D: decide how to cont.
                    if further is @ last 0 (aka tail)
                        prev.next = None and STOP
                    else:
                        prev = prev.next  # move further

            E: return head

        
        """
        ### HELPERS


        ### EC:
        # TODO

        ### DRIVER code
        if head:
            # A:
            prev, further = head, head.next

            # B: 
            while further.next:
                running_sum = rs = 0

                while further.next and further.val != 0:
                    rs += further.val
                    further = further.next

                # C:
                prev.val = rs

                # D:
                if further.next:
                    prev = prev.next
                    further = further.next
                else:
                    prev.next = None

            # E: 
            return head

"""
Input: [1,3,4 --> 
3,0,2,2,0]
            p         f

rs = 1,
     0, 3
     0, 2, 4

Output: [1,3,4]

"""