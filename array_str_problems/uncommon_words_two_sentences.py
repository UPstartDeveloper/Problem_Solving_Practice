from typing import List


class Solution:
    """Problem:

        We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

    A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

    Return a list of all uncommon words.

    You may return the list in any order.



    Example 1:

    Input: A = "this apple is sweet", B = "this apple is sour"
    Output: ["sweet","sour"]
    Example 2:

    Input: A = "apple apple", B = "banana"
    Output: ["banana"]


    Note:

    0 <= A.length <= 200
    0 <= B.length <= 200
    A and B both contain only spaces and lowercase letters.
    """

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        """
        return a list of words that are uncommon

        Input: A = "this apple is sweet", B = "this apple is sour"
        Output: ["sweet","sour"]

        words = this, apple, is, sweet, sour

        uncommon - word only appears once
        - in one sentence only ---> couldn't we just simplify it to be once overall

        Clarfications:
        - A or B can be empty
        - if not empty, A or B can contain only spaces or lowercase letters
        - do we need to return words in a specific order? yes
        - is it okay to use the built-in sort()?

        Assumptions:
        - words need to be sorted in relation to sentences, and to each other (if from the same sentence)
        - form a list of uncommon words in order from A, then form B, ---> then merge together fro the outpt

        Brainstorm:

        1. Brute force - frequency dist
        # A: form a dict of all the unique words in both sentences
        # B: enumerate how many times each unique word type appears
        # C: at the end, we return a subset of words w/ only one token
        # D: convert it to a list

        # uncommon - word that appears once and in only one sentence
        # unique - word that appears once in a sentence
             0      1      2    3
            [this, apple, is, sweet]
        A = "this apple is sweet", ----> {this: (0, 1), apple: (1, 1), is: (2, 1), sweet: (3, 1)}
                    -----> {this, 0, apple, 1, is, 2, sweet, 3} = setA
        B = "this apple is sour" ----> {this: 1, apple: 1, is: 1, sour: 1} = setB
        ------> {this, 0, apple, 1, is, 2, sour, 3}

        find the uncommon words in order, given set A and B

        unique_words = [setA, setB]
        return the intersection of both sets

        {(this, 0), (apple, 1), (is, 2), (sweet, 3)},  {(this, 0), (apple, 1), (is, 2), (sour, 3)}
        "this apple is sweet", "banananas are not"


        for each set
            for each word, order tuple in the set
                if the word doesn't appear in the other
                    add the tuple to the output list1


        Edge Cases:
        - what is one or both of the sentences is empty?
            - will we run into any index errors?


        Unused Code:
        def merge_uncommon_words(uncommon_list1, uncommon_list2):
            '''ensures the uncommon words are in order. Order of args matters!'''
            pass

        Time: O(A + B)
        Space: O(A + B)
        """

        def enumerate_words(word_list: List[str]):
            """form a frequency distributuion of words in a list"""
            type_tokens = dict()
            # enumerate both the place and number of tokens of the word type
            for index, word in enumerate(word_list):
                if word not in type_tokens:
                    type_tokens[word] = 1
                else:  # word seen before, increment the occurences only
                    type_tokens[word] += 1
            # return the dist
            return type_tokens

        def add_uncommon(uncommon, word_list, word_dict, other_dict):
            for word in word_list:  # w iterations
                # check if the word doesn't appear in the other sentence
                if word not in other_dict:
                    # and that if it appears only once in this sentence
                    if word_dict[word] == 1:
                        # add to the list
                        uncommon.append(word)

        # A: enumerate the words in A and B
        word_countA, word_countB = (
            enumerate_words(A.split()),
            enumerate_words(B.split()),
        )
        # B form the uncommon list
        uncommon = list()
        add_uncommon(uncommon, A.split(), word_countA, word_countB)
        add_uncommon(uncommon, B.split(), word_countB, word_countA)
        return uncommon


if __name__ == "__main__":
    # Test Cases:
    sentence_pairs = [
        # words repeated in both
        ("this apple is sweet", "this apple is sour"),
        # one sentence has no uncommon words
        ("s z z z s", "s z ejt"),
        ("apple apple", "banana"),
    ]
