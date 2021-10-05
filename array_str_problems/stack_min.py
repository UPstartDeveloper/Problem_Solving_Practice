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
- linear search for the minimum element, call after each push/pop
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

when min is deleted, how to find the next smallest

push 2
push 2
push 5
push 1
pop()
push 3

stack:
[2, 5, 1, -9 ,5, 6, 4]

min: -9

Helpful Hint from LeetCode (credit to @aakarshmadhavan):
"Consider each node in the stack having a minimum value."
"""


class MinStack:
    def __init__(self):
        """
        initialize the data structure. Using dynamic arrays.

        Every item in the min_nums array, is the smallest item.
        Out of itself and all its left neighbors.

        Adds O(n) space, and alls all methods to run in O(1) time.
        """
        self.stack = list()
        self.min = float("inf")
        self.min_nums = list()

    def push(self, x: int) -> None:
        """Add the new node the stack, and update the minimum."""
        # add the new number to the stack
        self.stack.append(x)
        # add the new number to the list of min nums
        if x < self.min:
            self.min = x
        self.min_nums.append(self.min)

    def pop(self) -> None:
        """Removes and returns the top node in the stack."""
        # remove the top elements on both arrays
        removed = self.stack.pop()
        self.min_nums.pop()
        # reassign the min property
        print(self.min_nums)
        if len(self.min_nums) > 0:
            self.min = self.min_nums[-1]
        else:  # assume no client will call min if no items in the stack
            self.min = float("inf")
        # return the removed item
        return removed

    def top(self) -> int:
        """return the top of the stack"""
        return self.stack[-1]

    def get_min(self) -> int:
        """get the min number property"""
        return self.min

    def is_empty(self):
        """Returns a boolean for there being 0 elements in the stack."""
        return len(self.stack) == 0


if __name__ == "__main__":
    # driver code from LeetCode
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    pass
