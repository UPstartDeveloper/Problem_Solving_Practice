'''
Problem: Find the 5th largest value in an array of n numbers.
'''

'''
1) load in first 5 elements into a sublist
    - keep track of the min of this sublist
2) traverse over the remaining elements
    - if an element is larger then the min,
        swap it in
    - update the min

3) return the min of the 5
'''

'''
Given an array a of numbers and a target value t, find two numbers that sum
to t (that is, a[i] + a[j] = t).

Given 2 arrays of n numbers each, find a pair of numbers (one from each array)
whose sum is closest to a given target value t.

Reverse a linked list by reusing the nodes (do not create new nodes).

Linked list
^                     ^
|                     |
(1) -> (2) -> (3) -> (4) ->

Linked

Stack:          Linked List
(1) ->          (2) -> (3) -> (4) ->

(2) ->          (3) -> (4) ->
(1)

(3)             (4) ->
(2)
(1)

(2)             (4) -> (3) ->
(1)

Output:
(4) -> (3) -> (2) -> (1) ->

Idea 1:



'''


'''
Find the k largest numbers in a an array of n numbers. Return them in an array
sorted in decreasing order.
'''

#  0  1  2  3  4
# [7, 6, 6, 4, 3, 2, 1] , k=4
# slice off up to k-1 index
# return the subset that goes from index 0-k1
# array[0:4]


def k_largest_numbers(array, k):
    return array[0:k]


print(k_largest_numbers([7, 6, 6, 4, 3, 2, 1], 4))
