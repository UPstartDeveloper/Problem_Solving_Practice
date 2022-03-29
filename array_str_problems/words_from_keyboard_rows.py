from typing import List


class Solution:
    """
    Suppose you're given a list of words. 
    Using this list, 
        return only the words that can be typed by using letters of the alphabet 
        on a single row 
        of a standard American “qwerty” keyboard

    Input: 
        - 1D list[str, immutable, upper/lower case english, dupe chars allowed]
        - ASSUME all words valid

    EC: 
        - [] --> []
        - non-valid word ---> not included in output
    
    Output: list[str]

    Intuition - arrays, hashmap
    
    Approach:

        A: map rows nums --> corr. letters
        B: check each input - if is_one_row_word(string)
            1: init a set of rows_needed_for_typing
            2: traverse the char of string --> add to the set
            3: return T/F len(set) == 1
        C: return output

    Big O:
        let n = # of element in word
        let l = longest word length
        O(n * l) for time and space
    """

    def words_from_keyboard_rows(self, words: List[str]) -> List[str]:

        ### HELPERS
        def _is_one_row_word(string, row_letters):
            # 1: traverse the char of string --> add to the set
            rows = set()
            for char in string:  # l iterations
                row_num = row_letters[char.lower()]
                if char.isalpha() is False:
                    return False
                elif row_num not in rows and len(rows) == 1:
                    return False
                rows.add(row_num)
            # 2: return T/F len(set) == 1
            return True

        ### MAIN
        # A: map rows nums --> corr. letters - TODO
        row_letters = {"a": 1, "b": 2}
        # B: check each input - if is_one_row_word(string) - > O(n * l)
        one_row_words = [
            word for word in words if _is_one_row_word(word, row_letters) is True
        ]
        # C: return output
        return one_row_words
