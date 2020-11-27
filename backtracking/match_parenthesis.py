def generate_parentheses(n):
    """
    generate all the different ways you can have n parentheses
    - nested
    - adjacent
    - mixture
    each of the combos is a str
    return an array of all the strings
    
    good case of backtracking
    
    n = 3
    
    two unique chars to wrry abouyt = '(' and ')'
    
    1st - 
        for _ in n, 
        add an opener
        for _ in n,
        add a closer
    ((()))
    
    
    2 options - add the next pair of parentheses adj, or nest it
    BUT we always add the open/close togetther!
    (())()
    
    Call Tree = n is the depth of the Tree
                1st           adj()
                            /            \
                2nd      nest()            adj() = '(())()'
                            /   \           /\
                3rd     nest()  adj()   nest()  adj()
                    '((()))'  '(()())
                
                '((()))
                
    Helper functions:
    1. nest() - adds inside the one we just added to the stack
    2. adj() - adds to the end of the string of the permutation
    
    n = is the var to use in ther logic
    base case:
        n = 0
        - pre: added all the ()
        - post: added the permutation to the output
    recursive case:
        - n > 0:
            add another () by adj()
            - recurse
            add another by nest()
            - recurse
            decrement n
            
    # Assume n > 1
    """
    global output
    def add_adj(permutation, parentheses_left):  # '()'
        # find the last ')' char
        for index_char in range(len(permutation) - 1, -1, -1):
            char = permutation[index_char]
            if char == ')':
                # add the new '()' next to it
                new_permutation = ''.join([
                    permutation[:index_char + 1], '()', permutation[index_char + 1:]
                ])
                generate_permutations(new_permutation, parentheses_left - 1)
                # return new_permutation
    def add_nested(permutation):
        # find the index of the last ')' char
        # '(())' 
        # ic = 3
        # last_closer_index = 3
        # c = 2
        # ci = 1
        # oi = 0
        for index_char in range(len(permutation) - 1, -1, -1):
            char = permutation[index_char]
            if char == ')':
                last_closer_index = index_char
                # while the index of the matching opener
                closers = 1
                closers_index = index_char - 1
                while closers_index > 0:
                    if permutation[closers_index] == ')':
                        closers += 1
                        closers_index -= 1
                    else:
                        break
                # find the index of the matching opening parenthesis
                opening_index = last_closer_index - (2 * closers) + 1
                # wrap the () in a new pair of parentheses
                new_permutation = (
                    permutation[:opening_index] + '(' + 
                    permutation[opening_index:last_closer_index + 1]
                )
                new_permutation += ')'
                return new_permutation
    def generate_permutations(permutation, parentheses_left):
        # base case: added n ()'s
        if parentheses_left ==  0 and len(permutation) == required_length:
        # append to the output
            if permutation not in output: 
                output.append(permutation)
            return
        # recursive case:
        while parentheses_left > 0:
            # add another by nest(), then recurse
            nested_permutation = add_nested(permutation)
            generate_permutations(nested_permutation, parentheses_left - 1)
            # add another () by adj(), and do so recursively
            adj_permutation = add_adj(permutation, parentheses_left)
            # generate_permutations(adj_permutation, parentheses_left - 1)
            # decrement n
            parentheses_left -= 1
            if parentheses_left == 0:
                return
    # init the output of all the permutations
    output = list()
    if n > 0:
        # save the required length in a global variable
        global required_length
        required_length = 2 * n
        # add the first parentheses
        permutation = "()"
        n -= 1
        generate_permutations(permutation, n)
    # return all the permutations
    return output
    
"""

output = [
'()()()',
'()(())',
'(())()',
'((()))',

]
n   |   permutation   |     ap      |     np    |   popped?
1         '()'        |     '()()'  |.  '(())'
------------------------------------------------------
0       '()(())  '       '()()()'.    '()(())'          X
------------------------------------------------------    
0                         '()()()'                      X
------------------------------------------------------
0       '()(())'                                        X
------------------------------------------------------
0         '(())'      |  (())()   |  '((()))'
------------------------------------------------------
0 `       '(())()'                                      X
------------------------------------------------------
0       '((()))'                                        X  

"""

if __name__ == "__main__":
    print(generate_parentheses(1))