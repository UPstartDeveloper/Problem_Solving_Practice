"""
stack of integers

# operations given as a string

# int x - 10000

pop - pops tops of stack

dupe - copies the number on top

plus + adds two topmost, adds sums ot the stack

(-) = removes the 2, subtracts 2nd from 1st and adds to stack

final - top of stack

Input

4 5 6 - 7 + -- string

Process:
push 4 []
push 5 , [4]

push 6, [4, 5]
        [4, 5, 6]
5 - 6
        [4, 1]
push 7
        [4, 1 ,7]
plus 
        [4, 8]

---> Final 8
-----------------
4 5 6 - 7 + -- string

[4, 8]


Intutition:
    - operations on a stack

Approach:
    - processing each command that comes

Edge Cases
    - positive #'s only
    - non-empty string
    - if stack is empty --> return None
    - ints
    - non-persistenet
#"""


class Stack:

    stack = list()

    def subtract(self):
        '''removes the 2, subtracts 2nd from 1st and adds to stack'''
        # check if 2 elements
        if len(self.stack) > 1:
            top = self.stack.pop()
            second = self.stack.pop()
            diff = abs(top - second)
            self.stack.append(diff)
            return 0
        else: 
            return -1

    def addition(self):
        '''adds two topmost, adds sums ot the stack'''
         # check if 2 elements
        if len(self.stack) > 1:
            top = self.stack.pop()
            second = self.stack.pop()
            self.stack.append(sum([top, second]))  # 5 + 6
            return 0
        else: 
            return -1

    def duplicate(self):
        '''copies the top elem, puts on the top'''
        if len(self.stack) > 0:
            top = self.stack[-1]
            self.stack.append(top)
            return 0
        else:
            return -1

    def solution(self, commands: str) -> int:
        # A: split up the chars 
        commands = commands.split()
        # B: process each char as a command
        char_functions = {
            "+": self.addition,
            "-": self.subtract,
            "DUP": self.duplicate,
            "POP": self.stack.pop, 
        }
        for char in commands:
            if char in char_functions:
                function = char_functions[char]
                # check if the func didn't fail
                result = function()
                if result == -1:
                    return -1
            else:  # is an int
                self.stack.append(int(char))
        # C: return the top int, or -1
        answer = -1
        if len(self.stack) > 0:
            answer = self.stack[-1]
        return answer


if __name__ == "__main__":
    # s = “4 5 6 - 7 +”  returns 8
    s = "13 DUP 4 POP 5 DUP + DUP + -"
    # s = "5 6 + -" 
    # s = “3 DUP 5 - -” return -1
    stack = Stack()
    print(stack.solution(s))


"""
[13, 13, 4] ---> result = 4

s = “5 6 + -” return -1

c
['5', '6', '+', '-']
                 ^
char_functions = {
    "+": self.addition,
    "-": self.subtract,
    "DUP": self.duplicate,
    "POP": self.stack.pop, 
}

char
5, 6, +, -

stack = [11]

result = 0

function = se

-----> -1
"""