"""
Problem


Test Inputs:

'aaa' - no spaces

'Hello World'  - space on one side

' World ' - spaces on both sides

"""

def length_of_last_word(words):
    """
    Returns the length of the last word (a string of lower or uppercase
    characters) from a string composed of space and alphabetic characters.

    Parameters:
    words(str)

    Returns: int

    """
    def traverse(index, progress):
        """
        Returns the index of a delimiter (either a space or the end/beginning 
        of the string).

        Parameters:
        start_index(int): the index to start iterating from
        progress(int): a postive or negative 1, to indicate what direction
                        to iterate in

        Returns: int: the modified value of start_index

        """
        # determine the stop condition
        if progress < 0:
            # iterating backwards
            STOP = STOP_INDEX_NEGATIVE
        else:  # progress > 0
            # iterating forwards
            STOP = -1
        # iterate
        while index != STOP:  # stops for words with no space
            # stop for words with space
            if words[index].isalpha() and words[index + progress] == " ":
                break
            else: 
                index += progress
        return index
    # useful constants for iteration
    WORDS_LENGTH  = len(words)
    STOP_INDEX_NEGATIVE  = -(WORDS_LENGTH)
    # find the index of the starting delimiter of the last word
    start = -1
    start = traverse(start, -1)
    # find the index of the ending delimiter of the last word
    end = start
    end = traverse(end, 1)
    # index the last word
    start += WORDS_LENGTH; end += WORDS_LENGTH
    last_word = words[start:end + 1]
    # return the length of the substring between the delimiters
    return len(last_word)

if __name__ == '__main__':
    # test case 1
    words = 'aaa'
    print(length_of_last_word(words))
    # test case 2
    words = 'Hello World'
    print(length_of_last_word(words))
    # test case 3
    words = ' World '
    print(length_of_last_word(words))
    # possible_space_index = start + progress
    # if words[possible_space_index] == " ":
