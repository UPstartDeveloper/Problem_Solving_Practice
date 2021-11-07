def backspaceCompare(String1, String2):
    """
    :type String1: str
    :type String2: str
    :rtype: bool

    Clarifying:
      - is it guaranteed the # will be <= the letters it
          comes after? --> No
      - only contain lower case letter and hashtags
      - is the input mutable? assume yes

    Idea #1 - iterative solution
    A: execute the backspaces
      while iterate backwards, if I reach a #
        count up how many there are
      from there, delete the #'s, and also delete up to
        the same amount in letters that came before

    B: check for equality
      then compare S and T

    Complexity:
    this solution would run in O(1) space

    however I don't believe the runtime would be linear,
    due to the time complexity of deleting substrings from
    S and T

    Idea #2
    we don't want to compare the str as given,
    but for what they become

    DP table
         a    b   #     c
      a  T    F   F     F

      d  F    F   F     F

      #  F    F   T     F

      c  F    F   F     T

    a####bc#d
    bd

    Idea 3: just look at letters after #

    but what would be done about letters between #, or
    letters before # that are not affected?

    BROKEN

    string  |   index   |   char    | pound_index | count_pound | string[pound_index]
    'ab#'   |     2     |     #     |     1       |   1         |
            |     0     |                                       | b
          start_delete = 1
    """

    def delete_pounds(string):
        index = len(string) - 1
        while "#" in string and index >= 0:
            print(f"Index: {index}")
            # discover a #
            char = string[index]
            if char == "#":
                # count up how many there are
                count_pound = 0
                pound_index = index
                while pound_index > -1 and string[pound_index] == "#":
                    count_pound += 1
                    pound_index -= 1
                # determine the start of the substring being deleted
                start_delete = pound_index - (count_pound)
                # resolve IndexErrors
                if start_delete < 0:
                    start_delete = 0
                if index > len(string) - 1:
                    index = len(string) - 1
                # perform deletion
                """if index == start_delete:
                    print(f'Index and Sd: {index,start_delete}')
                    string = string[start_delete]
                else:
                    string = string[:start_delete] + string[index + 1:]"""
                print(f"Index and Sd: {index,start_delete}")
                string = string[: start_delete + 1] + string[index + 1 :]
                # reset the index
                index = len(string) - 1
                print(f"String after deletions: {string}")
            else:
                index -= 1
        return string

        # difference between count_pound * 2, and number of letters
        # from pound_index and index 0

    # A: execute the backspaces on S and T
    String1 = delete_pounds(String1)
    String2 = delete_pounds(String2)
    # B: check for equality
    print(String1, String2)
    return String1 == String2


sampleInput1A = "ab#"
sampleInput1B = "ab#"
print(backspaceCompare(sampleInput1A, sampleInput1B))
