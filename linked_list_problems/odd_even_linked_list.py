# Leetcode problem description: https://leetcode.com/problems/odd-even-linked-list/


class ListNode:
    '''Definition for singly-linked list.'''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        """
        1-indexed
        
        .val? == index? NOPE
        
        Intuition: in-place, 2 pointers, 1 pass, head stays the same
        
        Approach:
        
         1.2 3.4 5 6 7
        [2,1,3,5,6,4,7]
         o e n t
         # A: store n.next in a temp
         # B: o.next --> n
         # C: n.next --> e
         2 3 1 5 6 4 7
           o n e t
         # D: e.next -> t
         # E: o = o.next
         1 2 3 4 5 6 7
         2 3 1 5 6 4 7
           o e n t
         2 
         
         2 3 5 1 6 4 7
             ^ 
        Edge Case: empty head --> return None
        
        loop while o is non-null
        # A: store n.next in a temp
        # B: o.next --> n
        # C: n.next --> e
        # D: e.next -> t
        # E: o = o.next
        
        [1,2,3,4,5]
         o e n t
         
         1
            3
               2
                  4 5
                  
        1, 3, 2, 4, 5
           o  e  n  t  
           3 
              4
                 2
                    5
        1, 3, 4, 2, 5  None
              o  e. n   t
              4
                 5
                    2
                      None
        1, 3, 4, 5, 2  None
                 o  e   n 
                 
        Idea: Reversing Pairs
        
        [1,2,3,4,5]
         ^ ^ ^
         
        [1,3,5, 4, 2]
             ^ ^ ^
             
        Brute Force:
        
        odds 
        evens
        
        One Pass - fill up both the lists
        
        Pass through odds
        Pass through evens
        
        Tail -> head
        
        # ##################
        A: init odd tracker and even tracker
        
        B: use 2 runners to traverse the list, group nodes into even/odd
        
        C: connect end of odd list to head of even list
        
        D: return head
        """
        if head is not None and head.next is not None:
            # A: init odd tracker and even tracker
            odd_head, even_head = head, head.next

            # B: use 2 runners to traverse the list, group nodes into even/odd
            odd_node, even_node = odd_head, even_head
            
            while odd_node is not None and odd_node.next is not None:
                # group the odd nodes
                odd_node.next = odd_node.next.next
                # stop the odd runner at the tail, so it can connect w/ even nodes
                if odd_node.next is not None:
                    odd_node = odd_node.next
                # group the even nodes
                if odd_node is not None:
                    even_node.next = odd_node.next
                    even_node = even_node.next
            
            # C: connect end of odd list to head of even list
            odd_node.next = even_head

        # D: return head
        return head  
        