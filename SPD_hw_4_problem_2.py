"""
Find the longest substring of unique letters in a given string of n letters.
"""


def get_substrings(text):
    '''Returns list of all unique substrings (letters only) in text.'''
    index = 0
    substrings = list()
    next_str = ''
    next_char = text[index]
    while next_char not in next_str and index < len(text):
        next_str += next_char
        substrings.append(next_str)
        index += 1
        next_char = text[index]
    return substrings


def find_longest_substring(text):
    # build a list of substrings
    substrings = get_substrings(text)
    # find the longest using linear search
    longest_length, index_of_longest = 0, 0
    for i in range(len(substrings)):
        length_of_next = len(substrings[i])
        if length_of_next > longest_length:
            longest_length = length_of_next
            index_of_longest = i
    return substrings[index_of_longest]


if __name__ == '__main__':
    text = "sleepy"
    print(find_longest_substring(text))
