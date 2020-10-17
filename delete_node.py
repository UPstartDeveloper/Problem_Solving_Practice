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
        
        
        # Idea #1
        # A: init stack
        stack = list()
        # B: push all nodes onto stack
        node = head
        while node is not None:
            stack.append(node)
            node = node.next
        # C: deletion
        # if the node being deleted is the head, 
        if n == len(stack):
            # modify the head
            if n > 1:
                new_head = stack[1]
                head = new_head
            else:  # n = 1
                # delete the last node
                head = None
        else:  # head stays the same, node in the middle or end is deleted
            # calculate the index where we expect the node BEFORE the one to delete is
            node_before_index = len(stack) - (n + 1)  # 1 - 2 = -1
            # grab a node at the before index
            node_before = stack[node_before_index]
            # deletion
            node_before.next = node_before.next.next
        # D: return the head
        return head
        """
        # Idea 2
        # init 2 pointers
        slow = head
        if head.next is not None:
            fast = head.next
        # iterate until the node being deleted (fast), node_before it
        while fast is not None:
            # move ahead both pointers
            slow = fast
            fast = fast.next
            # if node to delete is found
            if 
                # delete that node
                sl
        # return the head
        return head
        """