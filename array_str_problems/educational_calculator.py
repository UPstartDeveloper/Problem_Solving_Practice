"""
You are building an educational website and want to create a simple calculator. 
The calculator will only allow addition and subtraction of positive integers.

Given an expression string using the "+" and "-" operators like "5+16-2", 
write a function to find the total.

Sample input/output:

calculate("6+9-12") => 3
calculate("1+2-3+4-5+6-7") => -2
calculate("255") => 255

Assumptions:
positive integers
only +/-
input -> 1 string
output -> int
can NOT assume there's at least one operation
will Assume there's at least one operand
will not make assumptions about the sizes of operands 
no spaces
there may be commas ---> replace w/ "_"

int("1_000") = 1000 ✅
int("1,000") = 1000 🚩


Brainstorming:

Intuition:
- an operand is something that's fenced in by two non-numerical symbols

Approach:
# Base Case:
    # no more expression
    # return the result
# Recursive Case:
    # pick up the next operand, 
    # updates the overall result (default is +)

calculate("1+2-3+4-5+6-7") => -2

expr                operand        operator     result
"1+2-3+4-5+6-7"         1               +        0, 1
"+2-3+4-5+6-7"          2               +        1, 3
"-3+4-5+6-7"            3               -        3, 0
"+4-5+6-7"              4               +        0, 4
"-7"                    7               -        5, -2
""                    N/A             N/A        -2

"""

from os import name


def calculate(expression, result=0):
    def define_operation(expression):
        # init the operator flag to return
        is_addition = True
        # find the next operand and operator
        end_of_op = 0
        operators_seen = 0
        threshold = 1
        if not expression[0].isnumeric():
            end_of_op = 1 
        while operators_seen < threshold and end_of_op < len(expression):
            if expression[end_of_op] == "+" or expression[end_of_op] == "-":
                operators_seen += 1
            end_of_op += 1
        # split the expression 
        operation  = expression[:end_of_op - 1]
        expression = expression[end_of_op - 1:]
        # update the expression
        if operation[0] == "-":
            is_addition = False
        # get the operand
        operand = 0
        # if it's the first, take the whole
        if operation[0] != "+" and operation != "-":
            operand = int(operation)
        # otherwise take everything but the last operator
        else:
            operand = int(operation[1:])
        return operand, is_addition, expression
    # Base Case: no more expression
    if result == 0:
        expression = expression.replace(",", "_")
    if len(expression) == 0:
        # return the result
        return result
    # Recursive Case:
    else:  
        print(result)
        # pick up the next operand
        operand, is_addition, expression = (
            define_operation(expression)
        )
        # updates the overall result (default is +)
        if is_addition:
            result = result + operand
        else:  # subtraction time
            result = result - operand
        return calculate(expression, result)


"""
+9-12

opAnd     isAdd      EOO      OS      Thresh
  6          T       2       1       1

operation = "6+"

"""

if __name__ == "__main__":
    print(calculate("6+9-12"))  # => 3
    print(calculate("1+2-3+4-5+6-7"))  # => -2
    print(calculate("255"))  # => 255
