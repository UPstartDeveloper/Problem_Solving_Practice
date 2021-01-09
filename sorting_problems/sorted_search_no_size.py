import math


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
- if List.elementAt(i) > x, then you can return -1 if you've already 
  seen everything to the left of i (linear search)

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

    n <,>,= (log(n)) + (n / 2)

1. Modified Binary Search - "runners"
    - if there's no size attribute
        - do a linear search to find the size of the list (obviously slow)

    - have two runners
    - first moves one by one
    - second moves 2 at a time
    - purpose of this is that after n/2 iterations -> 1 is halfway through the list
                                                   -> 2 is either at the end, or just beyond
    - from there, you have the low, middle, and high to do binary search
    O((n/2) + log(n))

     0  1  2  3  4  5  6  7  8
    [1, 3, 3, 3, 5, 7, 8, 9, 9]
     ^  ^
        ^     ^
           ^         ^
              ^           ^
                 ^              ^



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
    
    def length(self):
        '''Return the length of self.nums. No built-ins!
         0  1  2   3
        [5, 3, 3] -1
        '''
        # A: init 2 pointers
        slow, fast = 0, 1
        # B: find where the second "falls off" the listy
        while (self.element_at(fast) != -1) and (self.element_at(fast + 1) != -1):
            #           T, F T, F                           T, T, F, F
            # C: move both ahead at different speeds
            slow += 1
            fast += 2
        # D: move the fast back until it's in bounds
        while self.element_at(fast) == -1:
            fast -= 1
        # E: return the length
        return fast + 1


class Solution:

    def sorted_arr_no_size_naive(listy, x):
        '''Performs linear search search for x in listy.'''
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

    def sorted_arr_no_size_binary_search(listy, x):
        '''Performs modified binary search for the index of x.'''
        def binary_search(low, high, target):
            # A: compare the elem at middle with target (x)
            while low <= high:
                # B: init the middle index
                middle = (low + high) // 2
                mid_elem = listy.element_at(middle)
                # if match -> return the middle index
                if mid_elem == target:
                    return middle
                # if middle > target -> search the lower half
                elif mid_elem > target:
                    high = middle - 1
                # if middle < target -> search the greater half
                elif mid_elem < target:
                    low = middle + 1
            # C: return -1 if it can't be found
            return -1
        # A: find out the length of listy in n / 2 iterations
        high_idx = listy.length() - 1
        # B: binary search from there
        return binary_search(0, high_idx, x)





"""
search for 3:
 0  1  2  3  4  5  6  7  8
[1, 3, 3, 3, 5, 7, 8, 9, 9]

i   e   answer = 2
0   1
1   3

 0  1  2  3  4  5  6  7  8  9
[1, 3, 3, 3, 5, 7, 8, 9, 9, 10]
             s               f
 l           m               h
 l  m     h  

high_index = 9, 3
low = 0, 0
mid = 4, 1
x = 3
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
    sol = Solution
    for x, ans in inputs:
        assert sol.sorted_arr_no_size_binary_search(array, x) == ans
