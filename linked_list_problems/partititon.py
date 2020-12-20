"""
Cracking the Coding Interview 2.4

Partition: Write code to partition a linked list around a value x, 
           such that all nodes less than x come before 
           all nodes greater than or equal to x. 
           
           If x is contained within the list, 
           the values of x only need to be after 
           the elements less than x (see below).
           
           The partition element x can appear anywhere in the 
           "right partition"; 
           it does not need to appear between the left and right partitions

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1[partition=5) 
          Left      |   Right
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Note: that only the sublist of nodes <5 are required to come before it -
      the rest can be anything

# do we have a singly linked or doubly linked list?
# do we need to swap the actual object, or just the value?

Ideas: 
1) use more memory
- collect all the node values in an array
- sort the array
- make a linked list from the array

- have two arrays
- iterate over the linked list
- sort each element into one or the other
- reconstruct a new linked list 

intuition: [3,2,1], [5,8,5,10]
            3 -> 2 -> 1 -> 5, 8, 5, 10
2) Swaps

intuition: swap elements less than p to the left
approach: 2 pters
        - find the size of the ll, 
        - and the number of elements < p
        - now, move the small elements you find on the right, to the left
        - init pointers at the first and last elements
        - for as many as needed # swaps
            - if pter on the left already in the right place, move forward
            - if pter on left and right wrong, then 
                - swap
                - increment
                - move the pters inwards
edge cases:
-
v                              v
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1

     v                         v
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1

          v               v
3 -> 1 -> 8 -> 5 -> 10 -> 2 -> 5

               v               v
3 -> 1 -> 2 -> 5 -> 10 -> 8 -> 5
--------------------------------
v              v
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1

     v                    v
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1

     v                    v
3 -> 2 -> 8 -> 5 -> 10 -> 5 -> 1

          v                    v
3 -> 2 -> 8 -> 5 -> 10 -> 5 -> 1

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def nums_smaller(self, parting):
        nums_smaller = 0
        node = self.head
        while node is not None:
            if node.data < parting:
                nums_smaller += 1
            node = node.next
        return nums_smaller

    def get_start_of_right(self, nums_smaller):
        node = self.head
        for _ in range(nums_smaller):
            node = node.next
        return node
        
    def partition(self, parting):
        '''move the small elements you find on the right, to the left'''
        # A: find the number of elements < p
        nums_smaller = self.nums_smaller(parting)
        # B: init pointers at the starting nodes of both partition
        left, right = self.head, self.get_start_of_right(nums_smaller)
        # C: for as many as needed # swaps
        fixes = 0
        while fixes < nums_smaller:
            # a) if pter on the left already in the right place
            if left.data < parting:
                #  move forward
                left = left.next
                fixes += 1
            # b) if pter on left and right in wrong spots
            elif left.data >= parting and right.data < parting:
                # i. swap
                left.data, right.data = right.data, left.data
                # ii. increment
                fixes += 1
                # iii. move the pters inwards
                left = left.next
                right = right.next
            else:
                right = right.next
        # D: exit the function
        return None 
"""
                                   r
               l       
3 -> 2 -> 1 -> 5 -> 10 -> 5 -> 8

ns = 3
f = 3

Time: O(n)
Space: O(1)
"""
