"""
Queue via Stacks

Implement a MyQueue class which implements a queue using two stacks.

Questions and Assumptions:

Model 1: Back to Back ArrayStacks
MyQ
               stack1 stack2
         t2                        t1
        [           ][ x1  x2  x3 x4]  
        f            ?            b

1. Interface:
    - enqueue
    - dequeue
    - front

2. Top Down
    - enq ----> popping from the front
    - deq ---> adding item to the end

3. Do the stacks have any size limits?
    - assume no
    - But,

4. Time Constraints on the Data Structure?
    - for now assume none

5. Should we account for error handling e.g. dequeing from an empty queue?

Break Down the Problem - is it possible to implement a q w/ 1 stack?
no, b/c LIFO not FIFO

        [x1 x2 x3 x4 x5]
                      t1

how to go from LIFO -> FIFO using a second stack?

Brainstorming:

1. use a second stack to reverse the first 
- fill up the first stack however much
- once it got full, pop all the items into another stack
- then if someone calls pop, pop normally from the second stack

        [x6             ]
                      t1
        [x5 x4 x3 x2 x1]
                      t2

Pros:
- slow 
- imposes size restrictions

2. Using a LinkedList to immplement the stack
- intuition: use stack2 to get access to the "bottom" stack1
- approach: 
    - enqueue - append to the tail of a ll
    - deq - delete head
    - front - return item at the end

Pros:
- resolves ambiguity about middle
- no size restrictions 
- fast

"""


class QueueNode:
    '''Regular to a node in a regular singly linked list.'''
    def __init__(self, val):
        self.val = val
        self.next = None


class MyQueue:
    def __init__(self, top: QueueNode):
        self.top, self.back = top, None

    def front(self):
        if self.top is not None:
            return self.top.val

    def enqueue(self, node: QueueNode):
        # TODO: test cases for all 3 scenarios; and refactor 
        # no current head
        if not self.top:
            self.top = node  
        # no current tail
        elif not self.back:
            self.back = node
        # adding a node after the current
        else:
            self.back.next = node
            self.back = node

    def dequeue(self) -> QueueNode:
        if self.top is not None:
            front = self.top
            self.top = self.top.next
            return front


if __name__ == "__main__":
    # A: init MyQ w/ no head or tail, then enQ
    q = MyQueue(None)
    x1 = QueueNode(1)
    q.enqueue(x1)
    assert q.top == x1
    assert q.top.next == None
    assert q.back == None
    assert q.top.next == q.back
    # B: init MyQ w/ a head, then enQ
    # C: enq after there's a head and tail
    pass

"""
top = None
back = None

List
____
"""
