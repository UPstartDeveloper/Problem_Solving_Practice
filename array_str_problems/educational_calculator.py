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

1. Iterating left to right, no space:
- init the operator to addition
- iterate over till you hit the next operator (or go out of bound)
    - update the result
    - update the operator
    - move on, 
- return the result


2. Iterating right to left
iterate until you hit an operator, 
    - push the operand and the operator onto a stack
    - push the last operand on w/ a plus

- pop everything from the stack, compute the result
- return the value

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
"2-3+4-5+6-7"          2               +        1, 3
"-3+4-5+6-7"            3               -        3, 0
"+4-5+6-7"              4               +        0, 4
"-7"                    7               -        5, -2
""                    N/A             N/A        -2

3. Using Two Operands Always

# A) init the result to 0 (will always be our first operand)
# B) init the operator based on if the first char (if not -, then +)
# C) iterate
    # get to the next operator sign (or the end)
    # take the 2nd operand (between operators, or from the beginning if first operation is addition)
    # do the operation(result, second_operand, operator), update result
    # update position of first operator
# D) return result

"1+2-3+4-5+6-7"
    ^
r = 1
o = +
so = 1
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


def calculate_optimal(expression):
    """
    # - return the result
    """
    """
    # - init the operator to addition
    is_addition = True
    # - iterate over till you hit the next operator (or go out of bound)
    start, end = 0, 0
    result = 0
    while start < len(expression):
        while end < len(expression):
            if not (expression[end] == "+" or expression[end] == "-"):
                end += 1
            else:
                break
        # - update the result
        if not is_addition:
            result -= int(expression[start:end])
        else:  # it is addition
            result += int(expression[start:end])
        # - update the operator
        if end < len(expression):
            is_addition = (expression[end] == "+")
        # - move on,
        end += 1 
        start = end
    return result
    """
    # A) init the result to 0 (will always be our first operand)
    result = 0
    # B) init the operator 
    first_operator_pos = 0
    # C) iterate
    second_operator_pos = first_operator_pos + 1
    while first_operator_pos < len(expression):
        # determine the operation we'll be doing
        is_subtraction = expression[first_operator_pos] == "-"
        # get to the next operator sign (or the end)
        while second_operator_pos < len(expression):
            # move ahead
            if not (expression[second_operator_pos] == "+" or 
                    expression[second_operator_pos] == "-"):
                second_operator_pos += 1
            else:  # hit the next operator
                break
        # take the 2nd operand - from the beginning if first operation is addition
        if first_operator_pos == 0 and is_subtraction is False:
            second_operand = int(expression[:second_operator_pos])
        else:  # (between operators)
            second_operand = int(expression[first_operator_pos + 1:second_operator_pos])
        # do the operation(result, second_operand, operator), update result
        if is_subtraction:
            result -= second_operand
        else:  # use additon
            result += second_operand
        # update position of first operator, and what it means
        first_operator_pos = second_operator_pos
        second_operator_pos += 1
    # D) return result
    return result
# calculate("6+9-12") => 3
# calculate("1+2-3+4-5+6-7") => -2
# calculate("255") => 255   


"""
+9-12

opAnd     isAdd      EOO      OS      Thresh
  6          T       2       1       1

operation = "6+"

"""

if __name__ == "__main__":
    print(calculate_optimal("6+9-12"))  # => 3
    print(calculate_optimal("1+2-3+4-5+6-7"))  # => -2
    print(calculate_optimal("255"))  # => 255
    print(calculate_optimal("-1+2-3+4-5+6-7"))  # => -2
