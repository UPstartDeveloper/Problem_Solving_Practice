"""
Three in One: 
Describe how you could use a single array to implement three stacks.

Clarifying Questions:

- is it a static array or dynamic array? 
    - assumme we're using a static array
- can we make any assumption about the number of items we need to have space for?
- can we mmake any assummption about the type of data the array will store?
- assuming we need to have a 1D array for the tri-stack
- Assuming we want O(1) time for the push pop peek methods
- Mental model?

MODEL: Shared Bottom, many tops
1. 1 Array, 1 Stack

[                ] ---> allows O(1) time for push, pop, peek, etc
                        b/c a Python list() always keep a reference to last element
0              n-1
bttm           top

2. 1 Array, 2 Stacks - sounds most similar to a deque (double-ended)
[                            ] ---> allows O(1) time for push peek, etc
                                  b/c a we'll keep pointers for both tops 
                                  (start at shared bottom)
                                 - assume we'll have 
                                   left-right variants of the ppp methods
0            mid           n-1
             bttm              
    top1                top2

push - overwrite the value at the index pointed to by the top, move the top away from btm
pop - return the value in the index pointed at by the top (if not none), move it closer to btm

3. 1 Array, 3 Stacks - "Tri-Stack"

Idea 1:
PQ - heap --> implemented using an array
- levels of the items in our queue = top
[("Hello", 3), ("world", 2), ("jumbo", 1) ]
---> WON't work becauuse we're raising the dims of the data
- also probably won't be able to meet the time constraints

Idea 2: 
allocate 1 half of the array for a uni-stack,
and the other half implements a di-stack

"""
