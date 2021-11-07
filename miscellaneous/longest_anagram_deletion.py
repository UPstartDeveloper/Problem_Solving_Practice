def longest_anagram(string, dictionary):
    longest_anagram = 0
    string_set = set(list(string))
    # useful constant for iterating
    STRING_LENGTH = len(string)

    def make_histogram(dict_word):
        # use a Python dict() type to map char types --> # tokens
        histogram = dict()
        for character in dict_word:
            # adding the first appearance of a character
            if character not in histogram:
                histogram[character] = 1
            # adding a character seen before
            else:
                histogram[character] += 1
        return histogram

    def is_anagram(dict_word):
        """Returns if the word in the dict is an anagram."""
        word_hist = make_histogram(dict_word)
        # determine if characters in the word are a subset of the string
        word_set = set(word_hist.keys())
        # and it's not longer than the input string
        word_chars = len(dict_word)
        # check that the characters are allowed (for it to be an anagram)
        if word_set.issubset(string_set):
            # check that the characters all appear in the correct amounts
            for key in word_hist:
                if not word_hist[key] <= string_hist[key]:
                    return False
            return True
        return False

    # make histogram of the string
    string_hist = make_histogram(string)
    # iterate over the dictionary words
    for word in dictionary:
        word_length = len(word)
        # determine if the word is an anagram made through deletion
        if is_anagram(word) is True:
            # make it the longest if appropiate
            if word_length > longest_anagram:
                longest_anagram = word_length
    return longest_anagram


if __name__ == "__main__":
    string = "batman"
    dictionary = ["bat", "aman", "antman"]
    print(longest_anagram(string, dictionary))
"""
Idea 1:

A: create histograms for each string in the dict - a iterations
B: create a set of letters in string - O(s)
C: compare which strings in dict are created through deletion - d iterations
  - their letters are a subset of the letters in string
  - their length is less than that of the string
D: find the longest string of the canidates

Time: 

s = length of input string
d = # of strings in the dict
a = # total letters of strings in dict
"""


"""
Idea 1:

A: create histograms for each string in the dict - a iterations
B: create a set of letters in string - O(s)
C: compare which strings in dict are created through deletion - d iterations
  - their letters are a subset of the letters in string
  - their length is less than that of the string
D: find the longest string of the canidates

Time: 

s = length of input string
d = # of strings in the dict
a = # total letters of strings in dict

Idea 2: 

- iterate over the dictionary 
- see if the word is an anagram
    - if it is, compute the length of the string
    - if > previous longest anagram, set that as new value
"""
