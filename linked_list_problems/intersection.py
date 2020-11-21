# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# yes to dupes

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        
        
        p1 == p2
        
        a: 1 -- 9---1--2--4
        b:          3--2--4
        
        # out of place #1 - store 2 array
        # out of place #2 - store 1 array (stack)
        
        # 2 pointer
        same length
        
        compare the addresses
        if !=, move them both up
        
            
        a: 1--9--1--2--4, 5
      ^
        b:       3--2--4, 3
                 ^
        
        2 linear passes, find the size
        3rd - find the intersection
        move up the p in the longer by difference
        if both pt's ==, or p1.next == p2
        
        """
        def calculate_size(head):
            # init size to 0
            size = 0
            # traverse from head to tail
            node = head
            while node is not None:
                size += 1
                node = node.next
            return size
        # 2 linear passes, find the size
        size_a = calculate_size(headA)
        size_b = calculate_size(headB)
        # 3rd - find the intersection
        pA = headA
        pB = headB
        difference = size_a- size_b
        # move up the p in the longer by difference
        if difference < 0:
            difference *= -1
            for _ in range(difference):
                pB = pB.next
        else:  # move up A
            for _ in range(difference):
                pA = pA.next
        # if both pt's ==, or p1.next == p2
        while pA is not None and pB is not None and pA != pB:
            pA = pA.next
            pB = pB.next
        return pA
    """
                   v
    listA = [2,6,4], sizeA = 3, 
                  v
    listB = [1,5], sizeB = 2
    
    d = 1
    
    """
