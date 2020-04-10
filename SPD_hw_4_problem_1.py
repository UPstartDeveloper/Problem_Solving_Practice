"""
Problem:
Given a string of text and a number k, find the k words in the given text that
appear most frequently. Return the words in a new array sorted in decreasing
order.

Problem Solving:
“One fish two fish red fish blue fish”

1 - form a histogram of the distribution of the word
hisotogram = {
    'one': 1,
    'fish': 4,
    'two': 1,
    'red': 1,
    'blue': 1
}

2 - convert to a list of lists
histogram.items() => [
    ('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)
]

3 - Choose the k largest tuples (based on word type count)

4 - sort that list

5 - pull out just the words from that list

"""


def get_duplicate_words(text, k):
    histogram = {}
    words = text.split()
    # make a distribution of word types and count of tokens
    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else:  # word type already seen before in histogram
            histogram[word] += 1
