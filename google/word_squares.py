"""
A “word square”:
- ordered sequence 
- K different words of length K
- when written one word per line, 
    reads the same horizontally and vertically. 

Example:
[
BALL
AREA
LEAD
LADY
]

Tasks:
1. det. given sequence of words is a word square (T/F)

Clarifications:
- bounds on K? ---> pos int
- words - only contain english letters
- case insensitive --> assume already all upper

Intuition:
    for all words in sq:
        - can use two pointers to determine if a word is in same pos, H/V
            - [constant row][all cols]
            - [all rows][constant col = constant row]

    FAIL FAST - if != --> return F, otherwise T comes at end

Edge Cases:

Approach:
    1. 2 pointers ---> K^2 / constant space

"""
from typing import List


class Solution:
    def is_word_square(self, words: List[str]) -> bool:
        # A: for all words in sq:
        for index in range(len(words)):
            # B: can use two pointers to determine if a word is in same pos, H/V
            word_row = words[index]  # read horizontally
            word_col = "".join(
                [  # read vertically
                    words[col_index][index] for col_index in range(len(words))
                ]
            )
            if word_row != word_col:
                return False
        # C: all words H/V same
        return True

    def get_all_word_squares(self, words: List[str]) -> List[List[str]]:
        """
        2. given an arbitrary list of words,
        return all the possible word squares it contains.
        (Reordering is allowed).

        Example:
        In: [AREA, BALL, DEAR, LADY, LEAD, YARD]
        Out: [
            (BALL, AREA, LEAD, LADY),
            (LADY, AREA, DEAR, YARD)
        ]

        Clarifications:
        1. assume all words have same length
        2. assumes that we have at least 1 word,
        3. no empty words

        Intuition:
            - decide on what K to use in the sq. ---> use the length of the words
            - what words to put in that sq. and in what order

        Approach:
            1. Brute Force:
                A: figure out what # of words to put in a square --> lengh of word
                B: try out all permutations of K words from the words list
                    C: test if it's a word sq.
                        D: if yes --> add a to list of word squares
                E: return all word squares found

        Edge Cases:
        1.
        """

        def get_square_length(words):
            """TODO:Use the length of the words -
            assume they all have same length"""
            return len(words[0])

        def form_all_squares(current_perm, sq_length, found, words):
            """ """
            # Base
            if len(current_perm) == sq_length:
                # C: test if it's a word sq.
                if self.is_word_square(current_perm) is True:
                    # D: if yes --> add a to list of word squares
                    found([word for word in current_perm])
            # Recursive - if len(current_perm) < sq_length
            else:
                for index in range(len(words)):
                    word = words[index]
                    current_perm.append(word)
                    remaining_words = [
                        rem_word
                        for rem_index, rem_word in enumerate(words)
                        if index != rem_index
                    ]
                    form_all_squares(current_perm, sq_length, found, remaining_words)
                    current_perm.pop()

        # A: figure out what # of words to put in a square --> lengh of word
        sq_length = get_square_length(words)
        # B: try out all permutations of K words from the words list
        all_squares = list()
        current_perm = []
        form_all_squares(current_perm, sq_length, all_squares.append, words)
        # E: return all word squares found
        return all_squares


if __name__ == "__main__":
    words = ["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]
    sol = Solution()
    print(sol.get_all_word_squares(words))
