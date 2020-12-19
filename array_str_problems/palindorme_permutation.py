"""
Cracking the Coding Interview 1.4: 

Palindrome Permutation: 
 
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
 
A permutation is a rearrangement of letters.
 
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)

# so if I understand correctly, we don't even have a dict right? yes
# palindrome DOES NOT include spaces!

Idea 1:
- calculate all permutations of the string,
- see which ones are palindromes
- return T/F if we can find at least one

Idea 2: 
- calculate if the string could be some permutation of some palindrome
- then we could say, would it be possible to make a palindrome out of this
- if len == even
    - do we have 2 tokens of each char type? --> T/F
- if odd --> T/F
    - even num of tokens for each type, 
    - except for one which is allowed to be odd

intution: use the freq dist of the alphabetical chars in the string
approach: use a dict to represent the dist, and the rules above
edge case: empty string ---> F, non-alphabetical char --> disregard

"""


def is_palindrome_permutation(string: str) -> bool:
    def make_frequency_distribution(string: str) -> dict:
        '''Maps each type of char to its tokens'''
        histogram = dict()
        for char in string:
            if char.isalpha() is True:
                # make comparisions case insensitive
                char = char.lower()
                # add to the histogram
                if char not in histogram:
                    histogram[char] = 1
                else:  # we've seen char before
                    histogram[char] += 1
        return histogram
    def could_be_palindrome(non_spaces, histogram):
        # set the allowed number of types that can have an odd # of tokens
        allowed_odd_types = 0
        if non_spaces % 2 > 0:
            allowed_odd_types += 1
        # iterate over the keys in the histogram, ensure it passes
        odd_types = 0
        for type, token in histogram.items():
            if token % 2 > 0:
                odd_types += 1
            # exit early 
            if odd_types > allowed_odd_types:
                return False
        return True
    # init the return value
    is_permutation = False
    # Edge Case: empty string ==> False
    if len(string) > 0:
        # A: create a histogram of the alphabetical chars in the str
        histogram = make_frequency_distribution(string)  # O(n) t/s
        # B: get the length of all non-space chars in the string
        non_spaces = len([char for char in string if char != " "])  # O(n) t/s
        # C: based on length and histogram, determine the return value 
        is_permutation = could_be_palindrome(non_spaces, histogram)  # O(n) t
    return is_permutation


"""     
          01234567
string = "Tact Coa"

ip = F

c = "a"
h = {
   "t": 2,
   "a": 2,
   "c": 2,
   "o": 1,
}

aot = 1
ot = 1

Time: O(n)
Space: O(n)
"""


if __name__ == "__main__":
    print(is_palindrome_permutation("Tact Coa"))
