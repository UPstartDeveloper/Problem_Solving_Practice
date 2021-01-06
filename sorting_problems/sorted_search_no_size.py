"""

Sorted Search, No Size: 
You are given an array-like data structure Listy, which lacks a size method.
It does, however, have an elementAt(i) method that returns the element at index i in 0(1) time. 
If i is beyond the bounds of the data structure, it returns -1. 
(For this reason, the data structure only supports positive integers.) 

Given a Listy which contains sorted, positive integers, 
find the index at which an element x occurs. 
If x occurs multiple times, you may return any index.

List ADT
- no size attribute
- constant time lookup operation
    - i > 0 or i >= 0 (assume i can be any nonnegative integer)

- sorted
- positive integets
- search for an element x
- or return the -1

Observations
- there can be duplicates (but we can return any single index)
- first index in Listy is always 0
- last index is always n - 1 (n = # elements)

Intuition:
- use binary search

Approach:
- use iteration to minimize space usage 

Edge Cases:
- what if the Listy is empty? 
    - check for that in the beginning, and return -1 if it's true


Brainstorming: 

0. Linear Search - linear time, constant space
    - start out at index 0
    - check each successive index until we find the element, or encounter -1

1. Modified Binary Search
    - if there's no size attribute
        - do a linear search to find the size of the list (obviously slow)


Test Inputs:

1)
search for 3:
 0  1  2  3  4  5  6  7  8
[1, 3, 3, 3, 5, 7, 8, 9, 9]

2)
search for 2:
 0  1  2  3  4  5  6  7  8
[1, 3, 3, 3, 5, 7, 8, 9, 9]

3)
search for 10:
 0  1  2  3  4  5  6  7  8
[1, 3, 3, 3, 5, 7, 8, 9, 9]

"""


class Listy:
    def __init__(self, arr):
        self.nums = arr
    
    def element_at(self, i):
        if 0 <= i < len(self.nums):
            return self.nums[i]
        else: 
            return -1


def sorted_arr_no_size(listy, x):
    '''Performs linear search search for x in listy, and return the index/-1.'''
    # A: init index at 0
    index = 0
    # B: iterate through indices of the Listy
    element = listy.element_at(index)
    while element != -1 and element < x:
        # increment the index and get the next element
        index += 1
        element = listy.element_at(index)
    # C: return the answer (assume that x was found)
    answer = index
    # if x was not found, then actually return -1
    if element != x:
        answer = -1
    return answer


"""
search for 3:
 0  1  2  3  4  5  6  7  8
[1, 3, 3, 3, 5, 7, 8, 9, 9]

i   e   answer = 2
0   1
1   3

"""


if __name__ == "__main__":
    inputs = [
        (0, -1), 
        (3, 1), 
        (2, -1), 
        (10, -1)
    ]
    array = Listy([1, 3, 3, 3, 5, 7, 8, 9, 9])
    # check if we get the right answer for each text input
    for x, ans in inputs:
        assert sorted_arr_no_size(array, x) == ans
