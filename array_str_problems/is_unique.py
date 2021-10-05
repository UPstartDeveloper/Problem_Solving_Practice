"""
1. Restate Problem
Given a string, determine if it has all unique chars?
Follow-up: how do it w/o additonal data structures?
- O(1) space?

2. Clarify Questions and Made Assumptions

"Hello World"
"cat" ---> ['a', 'c', 't'] --> 'act'
   ^ 
  ^

- string can have spaces? yes
- empty string? yes --> True
- any limits of types of chars? no
- sorting allowed? yes
- is the input mutable? yes
- is it case sensitive? assume yes
 Ccat --> T/F?

3. THINK

Intuition: 
- humans take a look at all - BCR is O(n)

Approach:

Idea - using a dict
1. Enumerate all types of chars in the stri
2. Return if each type has count of 1

Idea - pointers - trading space for quadratic time
1. for eachj letter, i
    - iterate backwards to check for duplicates

Idea - use in-place sorting algorithm
1. sort all the chars to begin
2. iterate forward, 
    a. iterate just one lettter behind

"""


class Solution:
    def sort_string(self, string: str) -> None:
        """
        Test:
        "cat"
        "act"
        tca

        index   cl   c     pi  pc
        1       0   'a'   0   'c'
                         -1
        2       2  't'   1      'c'
                         0      'a'

        Quicksort - nlog n -->
            Pros:
            - unstability is fine
            - in place
            Cons:
            - right idea of a pivot, --> risking quadratic runtoime

        Selection and Bubble

        TimSort(can't use built-in)
        HeapSort(can't use built-in)


        """
        # iterate over the string
        for index in range(1, len(string)):
            char = string[index]
            current_loc = index
            # backwards
            for previous_index in range(current_loc - 1, -1, -1):
                # swap as necessary
                prev_char = string[previous_index]
                if char < prev_char:
                    string[previous_index] = char
                    string[current_loc] = prev_char
                    current_loc = previous_index
        return string

    def is_unique(self, string: str) -> bool:
        """
        Time: O(n^2)
        Space: O(1)
        """
        # iterate over the string
        for index in range(len(string)):
            # iterate backwards to check for dupes
            char = string[index]
            for previous in range(index - 1, -1, -1):
                if char == string[previous]:
                    return False
        # if not failing, return True
        return True


"""
 012
"cat"

index     c     p
0        'c'    0  'c'
1        'a'    -1
2        't'    1   'a'
                0   'c'
3


"""


if __name__ == "__main__":
    strings = ["cat", "Hello World"]
    sol = Solution()
    for string in strings:
        print(sol.sort_string(string))
        print(sol.is_unique(string))
