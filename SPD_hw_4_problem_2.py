"""
Find the longest substring of unique letters in a given string of n letters.
"""


def find_longest_substring(text):
    # build a list of substrings
    substrings = list()
    index = 0
    while index < len(text):
        next_substring = [
            text[i] for i in range(len(text)) if text[i] not in text[:i]
        ]
        substrings.append(''.join(next_substring))
        index += len(next_substring)
    # find the longest using linear search
    longest_length, index_of_longest = 0, 0
    for i in range(len(substrings)):
        length_of_next = len(substrings[i])
        if length_of_next > longest_length:
            longest_length = length_of_next
            index_of_longest = i
    return substrings[index_of_longest]


if __name__ == '__main__':
    text = "I feel sleepy"
    print(find_longest_substring(text))
