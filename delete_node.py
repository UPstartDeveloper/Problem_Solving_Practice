# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Idea #1: stack
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        - is at least 1 node
        
        # Idea #1: stack
        
        A: iterate push all the nodes onto a stack
        bottom                          top
        [1, 2, 3, 4, 5,]
        B: pop off n + 1 times
        
            deleted_node - n = 3 --> ListNode(3)
            node_before --> ListNode(2)
        
        C: point the node_before.next --> node
        
        O(n) time 
        O(n) stack
        
        # Idea 2 - 2 pointers
        - find the node being deleted with one pointer,
        - track the node right behind it with another pointer
        - how to know when we hit the node being deleted?
            - 
        - whenever node being deleted is head 
            --> return the new head, 
            --> or None if no more remaining nodes
            - instead of just returning input head
             s f  
        [1,2,3,4,5]
               ^  
        s.next = f.next 
            
        best 
        { 
        1: 1,
        2: 2,
        3: 3
        4: 4,
        5: 5}
        
        Time: O(n) - 1 pass
        Space: O(n) 
         
        [1,2,3,4,5] - list
                 ^
        [1, 2, 3, 4] - stack
        """
        slow = fast = head
        # move ahead fast by n steps
        for _ in range(n):
            fast = fast.next
        # move both to right spots for deletion
        if fast is not None:
            while fast.next is not None:
                # move fast and slow
                fast = fast.next
                slow = slow.next
        if head.next is None:  # only 1
            head = None
        elif fast is None:  # head being deleted
            head = head.next
        else:
            slow.next = slow.next.next
        return head
