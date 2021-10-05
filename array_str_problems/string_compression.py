"""
String Compression: 

Implement a method to perform 
basic string compression using the counts of repeated characters. 

For example, the string 
aabcccccaaa ---> a2b1c5a3

If the "compressed" string would not become smaller than the original string, 
your method should return the original string. 

You can assume the string has only uppercase and lowercase letters (a - z).


Clarifying Questions and Assumptions:
1. only upper and lower case English letters
2. so our job is just to compress the substrings of repeated letters?
3. so our coefficient can never be 1? no, it can be 1
    abcd ---> abcd, not a1b1c1d1
    but what about 
    abbbbbbbbbbbbbcd ---> a1b13c1d1, or ab13c1d1

Edge Cases
1. empty string?

Intuition:
- we need to make a frequency distribution of some kind for the string,
- BCR - linear time
- BC space = linear, b/c strings are immutable in Python

Approach:
1. dict (but it won't work because order matters)
2. list of tuples
    aabcccccaaa ---> 
    [
        ('a', 2),
        ('b', 1),
        ('c', 5),
        ('a', 3)
    ] --->
    'a2b1c5a3' 
    ---> output

"""


def compress_string(string) -> str:
    """
    big O:
    linear time
    linear space
    """
    # validate the string
    if isinstance(string, str) is False:
        raise ValueError(f"Error while validating input. {string} is not of type str.")
    # compress the string
    output = string
    if len(string) > 0:
        # A: init a list
        str_counts = list()
        # B: populate it with counts (iterates over string)
        index = 0
        while index < len(string):
            # C: count the occurences of this letter
            letter = string[index]
            count = 1
            counting_ndx = index + 1
            while counting_ndx < len(string) and string[counting_ndx] == letter:
                count += 1
                counting_ndx += 1
            index = counting_ndx
            # D: insert in the freqency dist
            str_counts.append(f"{letter}{count}")
        # E: form the compressed string
        compressed = "".join(str_counts)
        # F: output the compressed string
        if len(compressed) < len(string):
            output = compressed
    return output


"""
Code Trace:
          0123456678901234
string = "abbbbbbbbbbbbbcd"
                          i

         abcdefghi
l = 'd'
c = 1

sc = [
    "a1",
    "b13",
    "c1",
    "d1"
]
"a1b13c1d1"
"""


if __name__ == "__main__":
    # abbreviate the function
    cs = compress_string
    # Test Inputs
    inputs = ["", "abbbbbbbbbbbbbcd", "aabcccccaaa"]
    # Outputs for the Test Cases
    outputs = [cs(string) for string in inputs]
    # Show the results
    for index, string in enumerate(inputs):
        print(f"{string} --> {outputs[index]}")
