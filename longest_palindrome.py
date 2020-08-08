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

def longest_palindrome(input_string):
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

if __name__ == '__main__':
    # Test Case 1
    print(longest_palindrome("cbbd"))
    # Test Case 2
    print(longest_palindrome("babad"))
    