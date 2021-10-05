"""
Sum Lists: 
You have two numbers represented by a linked list, 
where each node contains a single digit. 

The digits are stored in reverse order, 
such that the 1's digit is at the head of the list. 

Write a function that adds the two numbers 
and returns the sum as a linked list.

EXAMPLE 0    1    1
Input: (7 -> 1 -> -6) + 
       (  ->)
        ^
       (5 -> 9 -> 2). That is, 617 + 295. 
                               -617 + 
                                295
                               -322
       ^
Output: 2 -> 1 -> 9. That is, 912.

912 // 100 ---> 9
912 // 10 --> 91
912 // 1 --> 912

0
912 % 10 --> 2
912 // 10 --> 91
91 % 10 --> 1
91 // 10 --> 9
9 % 10 --> 9
9 // 10 --> 0


Clarifying Question:
- can we assume the linked lists will be of the same length always? no
- are we only dealing with positive integers? yes

Intuition:
- in the ideal situation, we have 3 linked lists of same length
- and they're both positive
- can just add the values in the nodes at end corresponding position, 
- carry over, until we reach the end of both lists and can use that to ma

Approach:
1. Traversing and Casting
A: make a float value from each list
    i. running sum, add to it by (node_val * current_power of 10, 
     muliply by -1 if needed)
B: sum the both
C: encode the sum as a list
    i. if the sum_val == 0 --> return a list of zero
    ii. go % / // by 10, while sum > 0

Edge Cases:
- 1 null list --> return thr list that's not null
- 2 null lists --> return a list of 0

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. 

EXAMPLE
Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).Thatis,617 + 295. Output: 9 -) 1 -) 2.That is, 912.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def sum_lists(listA: ListNode, listB: ListNode):
    """
    a = length A;  b = length B
    Time: O(a + b + max(a, b))
    Space: O(max(a, b))
    """

    def decode(list_head: ListNode):
        # init decoded value to zero
        decoded = 0
        # count the powers of 10 --> start at 0
        exponent = 0
        while list_head is not None:
            # add to it by (node_val * current_power of 10)
            node_val = abs(list_head.val)
            decoded += node_val * (10 ** exponent)
            # muliply by -1 if needed at the end
            if node_val < 0:
                decoded *= -1
            # move on to next iteration
            list_head = list_head.next
            exponent += 1
        return decoded

    def encode(sum_value) -> ListNode:
        # if the sum_val == 0 --> return a list of zero
        if sum_value == 0:
            return ListNode(0)
        else:  # sum_value is positive or negative int
            # ii. go % / // by 10, while sum > 0
            head_node, current_node = None, None
            # flag tells us if we want to put a negative at the end
            is_negative = sum_value < 0
            length = 0
            while abs(sum_value) > 0:
                next_node_val = abs(sum_value % 10)
                next_node = ListNode(next_node_val)
                # update the sum
                sum_value = sum_value // 10
                # add the next_node to the current list
                length += 1
                if length == 1:
                    head_node = current_node = next_node
                else:
                    current_node.next = next_node
                    current_node = current_node.next
            # if it is negative, modify the last node
            if is_negative is True:
                current_node.val = -1 * current_node.val
        return head_node

    # A: make a float value from each list
    num_listA, num_listB = decode(listA), decode(listB)  # O(a + b)
    # B: sum the both
    sum_value = num_listA + num_listB  # O(1)
    # C: encode the sum as a list
    return encode(sum_value)  # O(max(a, b) + 1)
