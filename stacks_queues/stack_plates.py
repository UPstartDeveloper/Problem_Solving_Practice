"""
Stack of Plates: Imagine a (literal) stack of plates. 
If the stack gets too high, it might topple. 

Therefore, in real life, we would likely 
start a new stack when the previous stack exceeds some threshold. 

Implement a data structure SetOfStacks that mimics this. 
SetOfStacks should be composed of several stacks and 
should create a new stack once the previous one exceeds capacity. 

SetOfStacks.push() and SetOfStacks.pop() should behave identically 
to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

Clarifying Questions:

1. So we need to design this data structure, which can hold 1 or mmore stacks in it? yes
2. Add the items in the stack are just plates? Do we need to implement a class for that too? no
re: push() and pop()
3. Is the client of this data structure supposed to let SetOfStacks know which stack they want
to push or pop from, when they call those methods -->
    - assume yes if there are multiple stacks
    - ok so if they specify it for us, will each stack have a unique identifier?
        - I guess we can handle letting the client know what stack names are available
        - and we can add them as we please, to make sure the ids work w/ dict() obj
4. So what do we do if they push a new plate, w/o specifying which stack to push to?
    - throw an error if there are multiple values?
    - OR what I can do is place it in the first stack I do have that isn't full yet, or else start 
         a new one if they're all full
5. What do we do if they pop a plate w/o specifiyng which
    - pop from the most recently pushed stack?
    - pop from the most recently created stack ---> assume this is the way to go, b/c it's simpler
6. Are there any limits on the number of stacks we can have --> no
7. Are we allowed to use the built-in dict class as part of SetOfStacks> --> assume yes for simpler


Intutition:
- let there be tons of stacks, constrain the size of each individual stack

Approach:

1. Dynamic Array for the stacks, each stack is an ArrayStack
2. Linked list of stacks, each stack is an ArrayStack
    - this is better because we will have no problem adding more stacks
    - however it will make lookups slow
    - but maybe we can fix that using a hash table

3. Dictionary that stores ArrayStacks
    - if no stack specified, then we iterate over the array stacks
    - can still add/lookup/remove array stacks quickly
    - but need to make sure each array stack has a unique identifier
        - add a list_stack_ids(), and a .num_stacks property
    - need to make an array stack class (wraps the Python list)?

Edge Cases:
- could we ever push anything other than a plate onto one of the stacks?
- what if they pass a id for a stack to push/pop, that doesn't exist?
    - check for that in push/pop ---> throw an error, tell client to
        take a look at the list_stack_ids() methods to get a sense 
        of what's available
"""
from typing import Tuple


class Plate:
    pass


class PlateStack:
    def __init__(self) -> None:
        self.plates = list()

    def push(self, plate) -> None:
        '''Add items to the end of the list (top of the stack).'''
        self.plates.append(plate)

    def pop(self) -> Plate:
        '''Remove from the end of the list (top of stack).'''
        return self.plates.pop()

    def is_full(self, cap: int) -> bool:
        return len(self.plates) < cap


class SetOfStacks:
    def __init__(self, capacity: int) -> None:
        self.stacks = dict()
        self.cap = capacity
        self.num_stacks = 0

    def list_valid_ids(self, purpose='push') -> list:
        """
        Give a zero-indexed list representing all stacks 
        that can be pushed or popped from.
        """
        # if pushing: return the id of each stack whose len < cap
        # if popping: return the id of each stack whose len > 0

    def _is_valid_id(self, id: int) -> bool:
        '''Returns T/F based on the id being a key of the stacks dict.'''
        pass

    def _find_stack(self, purpose='push') -> Tuple[int, PlateStack]:

        def _find_stack_push(self):
            '''returns the first PlateStack < cap'''
            # find the first available plate
            plates = sorted(list(self.stacks.items()))
            for plate_id, plate in plates:
                if plate.is_full(self.cap) is False:
                    return plate_id, plate

            # adding a new plate
            return self.add_plate()


        def _find_stack_pop(self):
            '''returns the first PlateStack > 0'''
            # TODO
            pass

        if purpose == 'push':
            return self._find_stack_push()
        return self._find_stack_pop()

    def _add_stack(self) -> Tuple[int, PlateStack]:
        '''TODO: add docstring'''
        plate_id, new_plate = self.num_stacks, PlateStack() 
        self.stacks[plate_id] = new_plate
        self.num_stacks += 1
        return plate_id, new_plate

    def _remove_stack(self):
        pass

    def push(self, plate, id=None):
        # A: init the stack
        plate_stack = None
        # B: find the right plate stack
        if id is not None and self._is_valid_id(id) is False:
            # print error message
            print(f"Cannot push to PlateStack at id {id}. \
                    Please use .list_valid_ids(purpose='push') to \
                    see which stacks are under capacity.")
        elif id is None:
            id, plate_stack = self._find_stack()
        elif self._is_valid_id(id) is True:
            plate_stack = self.stacks[id]
        # C: add the plate to the stack
        plate_stack.push(plate)
        # D: print message to say if stack is still < cap
        print(f"Successfully pushed to stack {id}")
        if plate_stack.is_full(self.cap):
            print(f"Stack {id} is now full.")
        
"""
FOLLOW UP
Implement a function 
popAt(int index) which performs a pop operation on
a specific sub-stack.
"""