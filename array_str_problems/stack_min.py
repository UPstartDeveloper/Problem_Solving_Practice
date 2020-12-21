"""
Stack Min: 

How would you design a stack which, 
in addition to push and pop, has a function min which returns the minimum element? 

Push, pop and min should all operate in 0(1) time.

Do we have a preference for whether the stack is implemented using an array or linked list? no

b               t
0   1  2  3  4  5
[9, 3, 1, 4, 2, 5]

push() - append an elem to the top of the stack. No return value
pop() - remove and return the last value at the top of the stack
min() - remove the smallest value in the stack (numbers, strings)

Brute Force min:
- linear search for the minimum element
    - obviously it's linear, so not going to work in O(1)

- Data Structure Brainstorm:
1. Pointer - stack keeps track of its min,
    - O(1) access
    - updated every push O(1)
    - update every pop (could become linear)

2. Min Heap
[1, 2, 3, 4, 6, 9]
    - O(1) min
    - updates would slow down push and pop - O(log n)

3. HashSet and Pointer
    - stack always keep track of its min O(1)
    - push - add elem to a set, and update min O(1)
    - pop - remove elem from set
        - if it's our min

4. Double-ended queue

Stack: [2, 2, 5, 3]

Hierarchy (deque): [2, 2, 5, 3]

min: 2

push 2
push 2
push 5
push 1
pop()
push 3

- pointer for the smallest value
- use a double ended queue for showing what the next smallests 

- what if someone pushes a new element that's greater than min, 
  but not the greatest?
- 

5. Hash Map

min: 1
Stack: [2, 2, 5, 1, 3]

hierarchy: every key maps to it's number of occurences, and next smallest

{
    1: (1, 2) --> next largest is the previous min
    2: (2, 5) --> next largest comes from recently added element
    3: (1, )
    5: (1, MAX) --> next largest hasn't yet come
}

push 2
push 2
push 5
push 1
pop()
push 3
"""
