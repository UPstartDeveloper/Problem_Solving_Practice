def valid(parentheses):
    """
    Validates if a string of only parenthetical characters 
    (aka those in the set of {'(', ')', '[', ']', '{', '}'})
    is in a valid order. 

    Parameters:
    parentheses: str

    Return: int: 0 means False, and 1 means True
    
    """
    # early exits: if there's an odd number of characters
    if len(parentheses) % 2 > 0:  # O(n)
        return 0  # the string must be invalid
    # convert the string to a list
    parentheses = list(parentheses)
    # map each closing parentheses to the appropiate opening
    closing_opening = {   # O(1)
        ')': '(',
        ']': '[',
        '}': '{'
    }
    # iterate over the input
    index = 0
    # precondition for while loop is that the string has even number of characters
    # best case: n/2, if the parentheses not enclosed, 
    # worst is n, when they are all enclosed, e.g. ((((((((((()))))))))))
    while index < len(parentheses):   # n iterations
        symbol = parentheses[index]
        # if it's a closing parentheses
        if symbol in closing_opening:
            # check that the opener is there, and in the right spot
            if index > 0 and parentheses[index - 1] == closing_opening[symbol]:
                # then delete both parentheses
                parentheses.pop(index)  
                parentheses.pop(index - 1)  # O( 2 * n/2 * n)
                # move on to the next iteration
                break
            # if the opening is not there, invalidate the string
            else:
                return 0
        # otherwise if we see an opening parentheses, just iterate
        else:
            index += 1
    # validate the string
    return 1