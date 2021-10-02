from typing import Optional

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem Description (credit to Leetcode): https://leetcode.com/problems/add-two-numbers/
        Input/Problem:
            - total _ sum  = 0
                --> ts + l1, += l2
                --> l1 + l2
            - return HEAD of the new list
            - 00099999
            - ASSUME:
                - last few nodes != 0 (leading zeros) - N/A
                - trailing zeros? 1,000,000
                    - yes
        EC:
            - l1.length != l2.length
            - sum of two nodes > 9
            
        Intuition:
            2 pointers
            decode: LL ---> int (keep track of exp of 10)
            encode: int ---> LL ()
            
        Approach:
        
            1) Pointers:
                A: decode 1st: LL ---> int (keep track of exp of 10)
                B: decode 2nd
                C: sum(1st, 2nd)
                D: encode sum
                E: return head of the summed LL
            
            encode:
                head pter = None
                calculate pow = 10
                modulo div of val % pow
                update the value ---> // pow
                add a new ListNode obj  (set head node as appropiate)
                
            time: TODO
            space: TODO
                
            342 % 10 ---> 2  # 1st node
            342 // 10 --> 34
            34 % 10 --> 4  # 2nd node
            34 // 10 --> 3
            3 % 10 --> 3 # 3rd node
            3 // 10 --> 0. # STOP b/c no leading 0
            
            
        
        """
        ### HELPERS
        def _decode(head):
            value, node, exp = 0, head, 0
            # figure out the value of the list
            while node is not None:
                value += (node.val * (10 ** exp))
                node = node.next
                exp += 1
            # return 
            return value
        
        def _encode(value):
            # special case:
            if value == 0:
                return ListNode(0)
            # A: head pter = None
            head, node = None, None
            # B: calculate pow = 10
            BASE = 10
            # C: making a new list
            while value:
                # modulo div of val % pow
                digit = value % BASE
                # update the value ---> // pow
                value = value // BASE  # //=?
                # add a new ListNode obj  (set head node as appropiate)
                if head is None:
                    head = node = ListNode(digit)
                else:
                    node.next = ListNode(digit)
                    node = node.next
            return head
        
        ### DRIVER
        # A: decode all
        addends = [_decode(head_node) for head_node in [l1, l2]]
        # B: sum(1st, 2nd)
        total = sum(addends)
        # C: encode sum, return the new list head
        return _encode(total)
    
    
"""
TEST:
l1 = [0], l2 = [0]
addends = [0, 0]
total = 0


l1 = [2,4,3], l2 = [5,6,4]
d         ^
      n
e =   0, 1,2
p =   1, 10, 100
v =.  2 + 40 + 300 = 342

total = 342+ 465 = 807 % 10 = 7
                   807 // 10 = 80
                   80 % 10 = 0
                   80 // 10 = 8
                   8 % 10 = 8
                   8 // 10 = 0 STOP
                   
                   
head = ---->ListNode(7), ListNode(0), LN(8)
node = --------------------------------^

"""
