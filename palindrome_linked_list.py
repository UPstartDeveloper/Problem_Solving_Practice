# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverse(self, head_second_half):
        """Reverses the order of ListNodes that come after the 
           input ListNode.

           Parameters:
           head_second_half (ListNode): a node in the middle of the 
                                        LinkedList

           Returns: the new head node of this section of the list

        """
        new_head = None
        while head_second_half is not None:
            # make a switch, using a temp variable
            node_after = head_second_half.next
            head_second_half.next = new_head
            new_head = head_second_half
            head_second_half = node_after
        return new_head


        
    def is_palindrome(self, head: ListNode):
        """
        assume numeric elements
        
        
        Idea #1 - list
            - store elements in a list
                iterate for n/2 
                    - iterate forwards and backwards, 
            
             0.  1.   2. 3
            [1 , 2,  2,  1]
                 
            Space: O(n)
            Time: O(n)
            
        head           |.  elements         | index | EL | ER 
        ListNode(1)    |    [1, 2, 2, 1]    |  1   | 2     2
        ListNode(2)
         ListNode(2)
         ListNode(1)
         None
        NUM_ELEM = 4
        
        """
        """
        # A: store in a list
        elements = list()  # O(1)
        while head is not None:  # n iterations  - O(n)
            elements.append(head.val)  # O(1)
            head = head.next  # O(1) 
            
        # B: check if its a palindrome
        NUM_ELEM = len(elements) # O(n)
        for index in range(NUM_ELEM // 2):  # range(0, 1)  # n/2 iterations 
            # get element from both forwards and backwards
            element_left = elements[index]
            index_right = NUM_ELEM - (index + 1)
            element_right = elements[index_right]
            # check for not palindrome
            if element_left != element_right:
                return False
        return True
        """
        """
        1->2->1
        
        Idea #2. - inside out
        
        Linked List class
            hashmap of index_nodex
            {  
                0: 1,
                1: 2,
                2: 2
            }
        - get_zero_ref(ListNode)  -> return the zero-index,
            
        
        - get node_from_index(index)  -> node
        A: find the middle element in the linked list
        B: get the left and right
            right: access .next
            left: the 
        
        # ordered - str(), list()
        # unorder - dict(), set(), 
        

        # A: convert to a tree-inplace
                    2 
                /      
            1
            
        STACK   
        
        # A: push all elememnts onto stack
            - O(n) time
            - (if in-place) - O(1 space)
        # B: pop
        B              T
        [1,  2 ,   2,  1]
        
        - top = 1
        
        #           Array vs. LL - Big 0
        #  lookup      O(1)     O(n) - linear
        #  space       constr   no constraints
        # 
        # list[n] = list[0]  + mem(1 elem) * index
        
        # 
        Idea #4:

        Insight: if a list is palindrome, then revered second half = first half

        A: find the number of elements
        B: calculate where the middle is, so we know where second half begins
            # store in a hash map
        C: reverse the second half
        D: compare each element in the first and second halves
            - return T/F based on each element is ==
        """
        """
        # A: find the number of elements
        num_elements = 0
        curr_node = head
        while curr_node is not None:
            num_elements += 1
            curr_node = curr_node.next
        # calculate where the middle node is
        MID_INDEX = num_elements // 2
        # keep a pointer to the middle element
        middle = head
        for i in range(MID_INDEX):
            middle = middle.next
        # C: reverse the second half (starts 1 node after middle)
        """
        """
        1->2->2->1->None

        ListNode: start_second_half   |   ListNode: tail    |
                    2                            1       

                problem: how to reverse a sublist in O(1) space?

            "going backwards" in a singly-linked list: use a stack


        """
        # D: compare each element in the first and second halves
        # return T/F based on each element is ==
        """
        DFS solution

        DFS(ListNode node) - head to start
            if .next property is None
                return value
            get value to compare with = call DFS on .next

        node     |      other        |      
        1                 
        2
        2
        1                 1
        
        """
        # Two Car solution
        # A: get two pointers at end, and middle of the list
        slower = faster = head
        while faster.next is not None and faster.next.next is not None:
            # move the pointers ahead
            faster = faster.next.next
            slower = slower.next
        # B: reverse the second half of the linked list
        head_second_half = self.reverse(slower.next)
        # C: Check that the two halves are equal
        while head is not None and head_second_half is not None:
            # find the mismatch
            if head.val != head_second_half.val:
                return False
            # otherwise move on to the next nodes
            head = head.next
            head_second_half = head_second_half.next
        # the list is palindromic
        return True


if __name__ == '__main__':
    # set up the list 
    nodes = [
        ListNode(1),
        ListNode(2),
        ListNode(2),
        ListNode(1),
    ]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    # test the solution (should be True)
    sol = Solution()
    print(sol.is_palindrome(nodes[0]))
    
            
        
  
        