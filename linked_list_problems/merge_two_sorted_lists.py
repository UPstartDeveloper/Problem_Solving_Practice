# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        - not stable
        - input is mutable
        
        - Intuition:
            2 pointers "battle" for the next node in the third LL
        - Approach:
        
        # start two pointers at heads of th list
            # if equal - take a copy of the first ll 
            # if not equal, take the lesser of the two
            # move ahead the pointer in whatever list wins
        # get to end of either of list --> load everything in the opposite
        
            
        
        l1 = [1,2,4], l2 = 
                     p1     
        l2 = [1,3,4]
                    p2
             
             winner = 1
             output = [1, 1, 2, 3, 4, 4 -->
             current_output = 1
            
        ListNode(1)
              
        output - 1 -> 1 -> 2 -> 4 -> 4 ->
        - Edge Case:
            - null list
            
        p1
        
        
        l1 = [1,1,2,3, 4, 4], l2 = 
                          p1     
        l2 = [1,3,  4]
                p3  p2
        """
        # test both nulls for the list
        if not l1:
            return l2
        elif not l2:
            return l1
        
        # start two pointers at heads of th list
        p1, p2 = l1, l2
        output_head = current_output = None
        while p1 and p2:  # min between (l1 and l2) in length
            # if equal - take a copy of the first ll 
            if p1.val <= p2.val:
                # set the winner, move ahead the pointer in whatever list wins
                winner = p1.val
                p1 = p1.next
            # if not equal, take the lesser of the two
            else:  
                winner = p2.val
                p2 = p2.next
            # add the new node to the output
            if output_head is None:
                output_head = ListNode(winner)
                current_output = output_head
            else:
                current_output.next = ListNode(winner)
                current_output = current_output.next
        # get to end of either of list --> load everything in the opposite
        unfinished = None
        if not p1:
            unfinished = p2
        elif not p2:
            unfinished = p1
        while unfinished:
            # add each each remaining node in that list
            current_output.next = ListNode(unfinished.val)
            current_output = current_output.next
            # move ahead the pointer 
            unfinished = unfinished.next
        return output_head
    
"""
Time: O(l1 + l2)
Space: O(l1 + l2)
"""
