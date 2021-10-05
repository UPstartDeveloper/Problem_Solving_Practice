"""
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold 
the additional characters, and that you are given the "true" length of the string. 

(Note: If implementing in Java, please use a character array so that 
you can perform this operation in place.)

EXAMPLE
Input: "Mr John Smith " J 13 
Output: "Mr%20John%20Smith"

13 = number of non-space chars? yes

So " " is not allowed as an input?

do we only put 1 %20 per space character, or 1 per each break in the tokens?
- 

Which kinds of characters count as part of string? anything that's not a space

should the function be implemented in place?

# intuition - add the %20 token for all the spaces that appear between words
# approach - using a while loop, adding in the enc char, and keep track of
#             how many letters (the real str) I've gone over
# to be more efficient, perhaps I can count up the number of space characters needed


# edge cases - beginng spaces - they don't count right? so if I see them 
#               I'll loop over it, so it doesn't influence how much of 
#               the string length my solution thinks it's gone over? 
                still add the special char

"4   gogogle   f " <-- input

space_chars = 8
true_length = 12
new_str_chars = [
    "4", "%20", "%20", 
]

''.join(new_str_chars)

"""


def urlify(string, true_length):
    # A: init the encoding token, and the new string
    ENCODING = "%20"
    # B: init array of chars for the new string
    new_str_chars = list()
    index = 0
    # get all the leading spaces
    while index < len(string):
        if string[index] == " ":
            new_str_chars.append(ENCODING)
            index += 1
        else:
            break
    length_seen = 0
    while index < len(string):
        char = string[index]
        if char == " ":
            new_str_chars.append(ENCODING)
        else:  # seen a letter
            new_str_chars.append(string[index])
        # increment the index, and length seen so far
        index += 1
        length_seen += 1
        # exit the loop early
        if length_seen == true_length:
            break
    # C: form the new string and return
    return "".join(new_str_chars)


"""
Input:    0123456789012
string = "Mr John Smith " 
TL = 13 

ENCODING = "%20"
new_str_chars = [M, r, "%20", "J]
index = 0, 1, 2, 3, 4
letters_seen = 0, 1, 2, 3
c = M, r, " ", "J"

Output: "Mr%20John%20Smith"
 "              "
# O(n) time
# Space O(n)
"""


if __name__ == "__main__":
    input = "Mr John Smith "
    tl = 13
    print(urlify(input, tl))
