def minAddToMakeValid(S):
    """
    Idea 1:
    - count up number of '(' chars
    - do the same for ')'
    - return the difference

    O(n) - time, O(1) space

    Idea #2 - expected indices

    - init count of min_needed = 0
    - iterate over the string
        - if '(' and count cuurently 0:
        - count up number of repeated '('
        - increment
        - elif ')' and count > 1:
        - count up number of repeated ')'
        - decrease the count by that amount
        - elif ')' and count == 0:
        - count up repeated ')'
        - increase by that amount

    """
    # count of minimum needed
    min_needed = 0
    # iterate over the string
    index = 0
    # useful constant
    STR_LENGTH = len(S)
    while index < STR_LENGTH:
        character = S[index]
        # increase min_needed by repeated characters
        if character == "(" or (character == ")" and min_needed == 0):
            count_char = 0
            # find number of repeated chars
            while index < STR_LENGTH and S[index] == character:
                index += 1
                count_char += 1
            # increase by that amount
            min_needed += count_char
        else:
            # otherwise decrease the min_needed
            while min_needed > 0 and S[index] == ")":
                min_needed -= 1
                index += 1
    return min_needed


sampleInput = "())"
print(minAddToMakeValid(sampleInput))


"""
       0  1  2  3  4  5
S =   '(  )  )  )  (  (

 index  |  character   |    min_needed
  2           )               2
"""
