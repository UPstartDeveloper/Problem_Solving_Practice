"""
Problem: https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/#!

Given:
- string S
- set of words D (kinda like a dictionary) 

find the longest word in D = subsequence of S.

Word W is a subsequence of S if:
- can delete some nonneg number of chars from W ---> S
- CANNOT reorder the chars 

Note: D can appear in any format: 
- list
- hash table
- prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, 
    but they are shorter than "apple".
The word "bale" is not a subsequence of S 
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

Clarifications:
1. Answer has to be valid word
2. and that == subseq
3. and we want to MAX L = length of that subseq found in D
4. Do we have any control over format of D?
    - no, but try w/ diff variations listed to practice Big O
5. word is not a subseq if we need to ADD letters to make it S

Example:
input of S = "abppplee" and 
         D = {
            "able", 
            "ale", 
            "apple",
            "bale", 
            "kangaroo"
        }

apple
    ^
abppplee
       ^

Intuition: 
    optimize L = length of a word in D that's also subseq of S

Edge Cases:
    - assume D is not empty
    - for now: D is a Python list
    - S is empty?
        - ""
    - multiple words w/ same longest length
        - either is fube
    - are no words that are subsequence?
        - ""

Approaches:
    List:
    1. Brute 
        - find all words that are a subsequence - 2 pointers
        - out of that --> find one that has longeest L - linear search
        - Time: D(L) + K(L), where
            - L = length of longest
            - D = # of words in dict
            - K = count of words that are a subsequence

    2. More Efficient
        - go over each word
            - decide if subseq or not
            - then right, figure out if that's the longests seen so far
        - Time: D(L)

    Set:

    Prefix Tree:

"""
from typing import List


class SolutionForLists:

    def is_subsequence(self, original, word):
        """
        able
             ^
        abppplee"
              ^
        r = F
        """
        result = False
        # see if all the letters in word, also appear in original 
        index_word, index_org = 0, 0
        while index_word < len(word) and index_org < len(original):
            # if letters same
            if word[index_word] == original[index_org]:
                index_word += 1
            index_org += 1
        # if reached end of word, then it is a subseqence
        if index_word == len(word):
            result  = True
        return result


    def find_longest_word(self, original: str, dictionary: List[str]) -> str:
        answer = ""
        longest_length = 0
        #  - go over each word
        for word in dictionary:
            if self.is_subsequence(original, word) is True:
                #  then right, figure out if that's the longests seen so far
                if len(word) > longest_length:
                    longest_length = len(word)
                    answer = word
        return answer


"""
"abppplee" 
D = {   
     word            index          is sub?
    "able",           <                 T
    "ale", 
    "apple",
    "bale",
    "kangaroo"  
}

answer      ll 
""          0      
""      
"""
S = "abppplee" 
D = {
    "able",     
    "ale", 
    "apple",
    "bale", 
    "kangaroo"  
}

sol = SolutionForLists()
print(sol.find_longest_word(S, D))
