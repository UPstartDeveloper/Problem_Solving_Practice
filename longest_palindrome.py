"""
def longest_palindrome(input_string):
    def is_palindrome(string):
        midpoint = int(len(string) / 2)
        LENGTH = len(string)
        for i in range(midpoint):
            front, back = (
                string[i], string[LENGTH - (i + 1)]
            )
            if front != back:
                return False
        return True
    # init a dict to keep track of the palindromes and lengths
    palindrome_len = dict()
    # iterate from both ends of the input_string towards the center 
    start, end = 0, len(input_string) - 1
    while start <= end:
        # get the letters both ends
        front, back = input_string[start], input_string[end]
        # get the letters next to those ends
        next_front, next_back = (
            input_string[start + 1],
            input_string[end - 1]
        )
        # if the letters match:
        if front == back:
            # and if the letters next to them match:
            if next_front == next_back:
                # see if the whole substring is a palindrome
                substring = input_string[start:end+1]
                is_pal = is_palindrome(substring)
                # if it is, then add it and the len() to dict
                if is_pal is True:
                    palindrome_len[substring] = len(substring)
                    break
        # otherwise, move the pointers
        # if end == the letter ahead the letter at front, move end
        elif back == next_front:
            end -= 1
        # elif front == the letter before the end, move front
        elif front == next_back:
            start += 1
        # otherwise move both inwards (next possible palindrome)
        start += 1; end -= 1
    # return the palindrome with the highest len
    lengths, palindromes = (
        palindrome_len.values(), palindrome_len.keys()
    )
    # print(palindrome_len)
    max_len = max(list(lengths))
    for palindrome in palindromes:
        length = palindrome_len[palindrome]
        if length == max_len:
            return palindrome
    """

def longest_palindrome(input_string):
    # A: init a dict to keep track of the lengths of palindromes
    len_palindromes = dict()
    def is_palindrome(substring):
        print(f'Checking if {substring} is a palindrome')
        midpoint = int(len(substring) / 2)
        LENGTH = len(substring)
        # early exit:
        if LENGTH < 2:
            return True
        for i in range(midpoint):
            front, back = (
                substring[i], substring[LENGTH - (i + 1)]
            )
            if front != back:
                return False
        return True
    def add_palindromes(start_index, end_index):
        # check if the substring is a palindrome
        substring = input_string[start_index:end_index]
        # check if we need another palindrome
        longest_pal_len = 0
        # determine if there's a palindrome length > remaining substr's
        if len(len_palindromes) > 0:
            longest_pal_len = max(list(len_palindromes.keys()))
        # we already have a longer palindrome,
        if longest_pal_len > len(substring):
            # so exit early
            return
        is_pal = is_palindrome(substring)
        # if it is, add it to the dict
        if is_pal is True:
            pal_length = len(substring)
            entry = (start_index, substring)
            # add as a new entry
            if pal_length not in len_palindromes:
                len_palindromes[pal_length] = [entry]
            # or add to a list of existing palindromes of same length
            else:
                # avoid adding duplicates
                existing_entries = len_palindromes[pal_length]
                if entry not in existing_entries:
                    existing_entries.append(entry)
            return
        else:  # substring is not a palindrome
            # also check and add palindromes from moving start index only
            add_palindromes(start_index + 1, end_index)
            # also check and add palindromes from moving end index only
            add_palindromes(start_index, end_index - 1)
            # and also try moving both indicies in
            # add_palindromes(start_index + 1, end_index - 1)
    # iterate from both ends of the input_string towards the center 
    start, end = 0, len(input_string)
    # B: get all the palindromes
    add_palindromes(start, end)
    # C: get the longest length palindromes
    longest_len = max((len_palindromes.keys()))
    longest_palindromes = len_palindromes[longest_len]
    # get the longest palindrome that appears earliest
    longest_palindromes.sort()
    index, palindrome = longest_palindromes[0]
    print(len_palindromes)
    return palindrome


if __name__ == '__main__':
    # Test Case 1
    # print(longest_palindrome("cbbd"))
    # Test Case 2
    # print(longest_palindrome("babad"))
    print(longest_palindrome("bbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    # print(longest_palindrome("racecar"))