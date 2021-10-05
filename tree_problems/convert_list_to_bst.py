import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_list_to_BST(head: ListNode) -> TreeNode:
    """
    - can have an empty head

    Assumptions:
    - values of the linked list are integers

    Input: head = ListNode(-10)
    list = [-10,-3,     0,      5,     9]
                    ^      ^       ^      ^

    Intuition:
    - recursively split the linked list in the middle (median)
    - make it the root of our tree

    Approach:
    # get all items in the linked list --> array
    # recursively form the trees
    # return the root of the whole tree

    Edge Cases:
    # empty head --> return None

    """

    def get_all_items(head):
        array = list()
        node = head
        # traverse the linked list
        while node:
            # append all the items into an array
            array.append(node.val)
            node = node.next
        return array

    def form_tree(items, low, high):
        # Base Case
        if low > high:
            return None
        # Recursive Case
        else:  # low <= high
            # calculate mid index
            mid = math.ceil((low + high) / 2)
            # get the middle element, create the root node
            root = TreeNode(items[mid])
            # set the left subtree       0      -1
            root.left = form_tree(items, low, mid - 1)
            # set the right subtree         1       0
            root.right = form_tree(items, mid + 1, high)

            # return the root
            return root

    if head is None:
        return None
    # get all items in the linked list --> array
    items = get_all_items(head)
    # recursively form the trees
    root = form_tree(items, 0, len(items) - 1)
    # return the root of the whole tree
    return root


"""
Time: O(n)
Space: O(n)
          0   1 2
items = [-10,-3,0]
low     high        mid  
0          2        1
0          0
            
       -3
    /       \
 -10        0

[-3, 0]

low     high        mid  
0          1        1
0          0


[0]
"""
