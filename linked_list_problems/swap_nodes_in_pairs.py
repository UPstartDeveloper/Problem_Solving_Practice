from typing import Optional

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
        

class Solution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Leetcode: https://leetcode.com/problems/swap-nodes-in-pairs/
        
        Input/Problem:
            SLL, mutable
            can be empty, even, odds
            
        Output:
            modified head 
            
        Intuition:
            swapping pointers (2 or 3)
            
        EC:
            1. no swapping required - < 2 nodes
            2. TODO
            
        Approach:
        
            DIY - O(n) time, O(1) space 
            
            A: Single Swap
                (outside of while) prev, node1, node2 = None, head, head.next
                
                temp = node2.next
                (if prev) prev.next = n2
                node1.next = temp
                n2.next = node1
               
                
            (If 1st swap) head = n2
             
            B: Moving to the next swap
                prev = n1
                n1 = t
                n2 = (if n1) n1.next
               
               
               
            1 --> 2 --> 3 --> 4 -->
       p   n1     n2.  t
           
            2 --> 1 --> 3 -- 4 -->
       p    n2    n1    t
                  p     n1.  n2     t
                  
            2 --> 1 --> 4 --> 3 --> 
                              p.    n1
        """ 
        if head is not None:
            # A: init values
            prev, n1, n2 = None, head, head.next
            # B: makes the swaps
            while n1 and n2:
                # 1) do a single swap
                next_n1 = n2.next
                if prev is not None:
                    prev.next = n2
                n1.next = next_n1
                n2.next = n1
                # 2) 1st: modify head
                if prev is None:
                    head = n2
                # 3) move on
                prev = n1
                n1 = next_n1
                if n1 is not None:
                    n2 = n1.next
        # C: all done!
        return head
