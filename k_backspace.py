def k_backspace(input_string) -> int:
    s_index = len(input_string) - 1
    # iterate in reverse
    while s_index > 0: 
        # check for backspace
        char_right = input_string[s_index]
        print(f'Right char: {char_right}')
        if char_right == '<':
            # track the end of the backspace sequence
            end_backspaces = s_index
            # find the start of the sequence
            while input_string[s_index] == '<':
                s_index -= 1
            # now calculate where the index should move (beyond the deletion)
            index_before_sequence_to_delete = (
                end_backspaces - (2*(end_backspaces - s_index))
            )
            print(index_before_sequence_to_delete, end_backspaces)
            # delete the backspaces and appropiate letters
            input_string = ''.join([
                input_string[i] for i in range(len(input_string))
                if not index_before_sequence_to_delete < i < end_backspaces + 1
                ]
            )
            print(f'Changed the string: {input_string}')
            # move the s_index again
            s_index = len(input_string) - 1
            print(f'moved to index {s_index}')
        else:
            # move one index back
            s_index -= 1
            print(f'moved to index {s_index}')

    return input_string

if __name__ == '__main__':
    input_string = 'foss<<rritun'
    print(k_backspace(input_string))
    
      
"""
01234
a<bc<

s_index |  char_right. | end_backspaces  |  index_before_sequence_to_delete
   3          <               4                     2
   2
   1
   
"""

"""# don't forget to actually call your answer's function!
testInput = 'a<bc<'
actualOutput = k_backspace(testInput)
print(actualOutput)"""

"""
Assume:
- string has only:
  - lower case English alpha
  - <
  
  


Insights:
- sequences of < 
- sequences of letters
- at some point, the letter is adjacent to <

Idea #1:

s = # letters in the string
i = index where the < is found 

Worst Case input:
aaaaaaaaa<<<<<<<<<<

- while < exists in the string:  - O(s) 
  - iterate the string in reverse - O(s)
    - if you find a < to the right of a letter:
        - then delete both characters from string - O(s - i)
        
Idea #2:

aaaaaaaaa<<<<<<<<<<

b = # of backspaces

- iterate the string in reverse: - O(s)
  - if you find a <:
      keep a count of how many found (keep index of where the sequence ends) - O(1)
      keep track of its index, of the first <
      - when you get to the letter, delete as many letters (as the backspaces needed to delete) - O(b * (s-i))


Indices After Deletion:
01234
aaa<<
"""

'''Alternative Solution that uses expression as a Stack'''
class StackSolution:
    def evalRPN(self, expression: List[str]) -> int:
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x
        def multiply(x, y):
            return x * y
        def divide(x, y):
            return x // y
        # map operation functions to characters
        op_char_func = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
          }
        OPERATORS = list(op_char_func.keys())
        # reverse the list
        expression.reverse()
        # use the expression as a stack, iterate in reverse
        index = len(expression) - 1
        while len(expression) > 2:
            # check for the first calculation
            possible_int1, possible_int2, possible_operator = (
            expression[index], expression[index - 1], expression[index - 2]
            )
            # make sure we have integers (in str data type)
            operands_valid = True
            try:
                possible_int1 = int(possible_int1)
                possible_int2 = int(possible_int1)
            # if it fails, then move on to the next set of three elements
            except ValueError:
                # move on the next index 
                operands_valid = False
            # also have to validate the operator
            if possible_operator in OPERATORS and operands_valid is True:
                # do the calculation
                operation = op_char_func[possible_operator]
                result = operation(possible_int1, possible_int2)
                # place the result into the expression
                expression.pop(index)
                expression.pop(index - 1)
                expression.pop(index - 2)
                expression.insert(index -2, result)
                # if you reached the bottom of the stack, start over at top
                if index == 2:
                    index = len(expression) - 1
                    break
                index -= 1
        # return final result
        return expression[0]
