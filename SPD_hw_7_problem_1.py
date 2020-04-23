'''
Problem Description and Starter Code on LeetCode website:
https://leetcode.com/problems/add-two-numbers/
'''


class ListNode:
    '''Definition for singly linked list.'''
    def __init__(self, x):
        self.val = x
        self.next = None


'''
Variable Table 1:
variable    | node   |  place_val  | increment |  return value         |
values      | First Call:                                              |
            | ( 2 )  |    0        |    2      |   2 + decode((4), 1)  |
            | ( 4 )  |    1        |    40     |   40 + decode((3), 2) |
            | ( 3 )  |    2        |    300    |   300 -> overall value is 342!
            | Second Call:                                             |
            | ( 5 )  |    0        |    5      |   5 + decode((6), 1)  |
            | ( 6 )  |    1        |    60     |   60 + decode((4), 2) |
            | ( 4 )  |    2        |    400    |   400 -> overall value is 465!

'''


def decode(node: ListNode, place_val=0) -> int:
    # calculate the decimal value of this single node
    increment = node.val * (10 ** place_val)
    # base case: we have reached the end of the linked list
    if node.next is None:
        return increment
    # recursive case: we move on the next node
    return increment + decode(node.next, place_val + 1)


'''
Variable Table 2:
variable    |    l1     |     l2     |    value1    |    value2   |   summed_val   |     places    |      value_left     |
values      |   ( 2 )   |     (5)    |     342      |     465     |    807         |      1        |          807        |
            |           |            |              |             |     |          |      2        |          80         |
            | _________ |  ________  |  __________  |  ________   |     v          |      3        |          8          |
            | head_node | prev_node  |    node      |      i      |     80         |
            |  ( 7 )    |    ( 7 )   |     ( 0 )    |      1      |     8          |
            |           |    ( 0 )   |     ( 8 )    |      2      |     0          |
'''


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # decode list1 to the equivalent decimal value
    value1 = decode(l1)
    # decode list2 to the equivalent decimal value
    value2 = decode(l2)
    # sum the two
    summed_val = value1 + value2
    # count up number of nodes needed for new list
    places = 1
    value_left = summed_val
    while value_left >= 10:
        value_left //= 10
        places += 1
    # init a head node to return at end
    prev_node = head_node = ListNode(summed_val % 10)
    summed_val //= 10
    for i in range(1, places):
        node = ListNode(summed_val % 10)
        prev_node.next = node
        prev_node = node
        summed_val //= 10
    # return the head of the new list
    return head_node


if __name__ == '__main__':
    # instantiate "good case" test inputs
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    # test that the function works
    assert add_two_numbers(l1, l2).val == 7
    assert add_two_numbers(l1, l2).next.val == 0
