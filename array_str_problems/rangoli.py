from string import ascii_lowercase


def print_rangoli(size):
    """
    Input/Problem:
        int ---> 1-26 inclusive
        tells us which letters to include
        all lowercase
        immutable
        
        ASSUME allowed ot use str.ascii_lowercase
    Output:
        str
        lines separated by newlines
        letters in a line - sep by "-"
        
    Intuition:
        iteration using a for loop + logic
        
    EC:
        int out of range --> ValueError
        
    Approach:
        output needs to have N * 2 - 1 lines
        for iter i, going from 1 - N: ADD letters
            start from Nth letter
            go backwards in the alpha, as many as i
            then add the reverse
        for iter i, going from N + 1 to STOP: RM letters
            start from ath letter
            go fwd in the alpha, as many as i
            then add the reverse
        always:
            join using "-"
            outer pad "-" until we have (4N - 3) chars in total
            add to array of lines
            
        return a single str, join using "\n"
    """
    ### HELPER
    def _padded(line):
        # define padding params
        WIDTH = 4 * size - 3
        num_dashes_on_each_side = nd = (WIDTH - len(line)) // 2
        # add the dashes
        dashes = "".join(["-" for _ in range(nd)])
        return "".join([dashes, line, dashes])

    def _next_line(i, letters):
        # i. compute how many letters needed
        length = i - size
        if i < size + 1:
            length = length * -1
        # ii. take the letters
        letter_subset = LETTERS[length:]
        # iii. make the full line
        first = "-".join(reversed(letter_subset[1:]))
        second = "-".join(letter_subset[1:])
        line = "-".join([first, letter_subset[0], second])
        # iv. get the right line length by padding
        return _padded(line)

    ### MAIN
    # A: init output arr
    lines = list()
    if size == 1:
        print("a")
        return
    if 0 < size < 27:
        # B: compute params of rangoli
        HEIGHT = size * 2 - 1
        LETTERS = ascii_lowercase[:size]
        # C: form the the lines
        line_num = ln = 1
        while ln <= HEIGHT:
            # add to output
            lines.append(_next_line(ln, LETTERS))
            ln += 1
    # D: combine rangoli into a single string
    output = "\n".join(lines)
    print(output)


if __name__ == "__main__":
    pass
