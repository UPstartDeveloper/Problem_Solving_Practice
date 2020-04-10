"""
Find the longest substring of unique letters in a given string of n letters.
"""


def get_substrings(text, substrings=[], index=0, next_sub=''):
    '''Returns list of all unique substrings (letters only) in text.'''
    # Base case: return all substrings
    if index == len(text):
        print(substrings)
        return substrings
    else:  # index < len(text)
        next_char = text[index]
        # add on to the next substring being added
        if next_char not in next_sub:
            next_sub += next_char
        # repeat letter found
        else:
            next_sub = ''
        # move on in traversing text
        index += 1
        substrings.append(next_sub)
        return get_substrings(text, substrings, index, next_sub)


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
