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


def build_histogram(text):
    '''Builds a distribution of the word types and numbers of word tokens.'''
    histogram = {}
    words = text.split()
    # make a distribution of word types and count of tokens
    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else:  # word type already seen before in histogram
            histogram[word] += 1
    return histogram


def find_min_and_its_index(largest_pairs):
    '''Linear search for the minimum word-count pair.'''
    current_min_index, current_min = 0, largest_pairs[0][1]
    for i in range(1, len(largest_pairs)):
        next_count = largest_pairs[i][1]
        if next_count < current_min:
            current_min = next_count
            # we keep track of the index of the overall tuple
            current_min = i
    return current_min_index, current_min


def find_largest(word_counts, count):
    """Iterates over a list of tuples, i.e. [('word': count_num)], and returns
       the subset of tuples with the largest counts, size count elements.
       Return value is given in decreasing sorted order.

    """
    # start by pre-loading the first pairs in the list, for as many as count
    largest_pairs = word_counts[:3]
    # keep track of the smallest pair in this list (linear search)
    current_min_index, current_min = find_min_and_its_index(largest_pairs)
    # find the true count-many word pairs in the list
    for i in range(3, len(word_counts)):
        # compare the next word count pair, to the minimum of the largest
        next_pair = word_counts[i]
        next_count = word_counts[i][1]
        # replace the current minimum in largest pairs, if necessary
        if next_count > current_min:
            largest_pairs[current_min_index] = next_pair
            current_min_index, current_min = (
                find_min_and_its_index(largest_pairs))
    return largest_pairs


def get_frequent_words(text, count):
    """A variation of the n-choose-k problem, which also involves sorting.
       Assumptions:
        1) the text contains alphabetic characters, with spaces in between
        2) Each word type has a distinct number of tokens associated with it
        3) word types are case insensitive, i.e. "one" = "One"

    """
    # build a distribution using a hashtable data type
    histogram = build_histogram(text)
    # find the k-largest mappings
    largest = find_largest(histogram.items(), count)
    # sort the largest_pairs in descending order
    # return just the words


if __name__ == '__main__':
    text = 'One fish two fish red fish blue fish'
    count = 3  # expected k <= number of word types
    get_frequent_words(text, count)
