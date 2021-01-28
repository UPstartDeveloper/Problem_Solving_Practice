from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        is_subset - every letter in this word, appears in the same or more amt
                in the larger word
                
        universal - this word is a superset of all words B
        
        
        Example:
                        F       F       T           T       T
        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o",]
        
        Output: ["facebook","google","leetcode"]
        
        
        Assumptions:
        - A and B are not empty
        - the strings in A and B are never empty
        - the strings only have lowercase letters
        - A and B are unique
        
        Clarifying :
        - order of ouput matter?
        
        Edge Case:
        - when either 
        
        Intution:
        - check if a word is a subset just by comparing freq dist of the chars
        
        Approach:
        # start w/ a new array of univ
        # for each a:
            # fail fast to see if it's universal - for each b
                # make a histogram of b
                # compare w/ the histogram of a --> is_subset(a, b)
            # if it is univ --> add it to array of univ word
        # return the new array
        
        univ = []
        
        a = "amazon", "o"
        {
            a: 2
            m: 1
            z: 1,
            o: 1,
            n: 1
        }
        
        wrr" is a subset of "warrior
            
        """
        def is_dist_same(a_hist, b_hist):
            for char_b in b_hist:
                counts_b = b_hist[char_b]
                if (char_b in a_hist and a_hist[char_b] < counts_b) or char_b not in a_hist:
                    return False
            return True
        
        def make_histogram(word):
            hist = dict()
            for char in word:
                if char not in hist:
                    hist[char] = 1
                else:  # in hist
                    hist[char] += 1
            return hist
        
        def is_subset(a_hist, b_hist):
            # check if the histograms are equal
            return is_dist_same(a_hist, b_hist)
        
        def combine(B):
            # init a hist for combined word
            combined = dict()
            # iterate over all b's
            for b in B:  # b iterations
                # make b's hist
                b_hist = make_histogram(b)  # O(b_long)
                # iterate over mini_b_hist, update combined_b_hist
                for char_b in b_hist:  # b_long iterations
                    if (char_b not in combined) or (combined[char_b] < b_hist[char_b]):
                        combined[char_b] = b_hist[char_b]
            return combined
        
        # start w/ a new array of univ
        univ = list()  # constant
        B_hist = combine(B) # O(b*b_long), b_long = length of longest in b
        for a in A:  # a iterations
            # fail fast to see if it's universal 
            a_hist = make_histogram(a)  # O(a_long), a_long = length of longest in a
            if is_subset(a_hist, B_hist): # O(b*b_long)
                univ.append(a)  # constant
        # return the new array
        return univ  # constant
    
    """
    Time:
    O(a(a_long + (b * b_long)))
     Space:
    O(a_long + b_long + a + (b * b_long))
    """
    
"""
Input:
A = ["amazon","apple","facebook","google","leetcode"], 
B = ["ec","oc","ceo"]

Output: ["facebook","leetcode"]

univ    |   a        |     b       | 
[]          amazon          ec
            apple           oc
            facebook

a_hist = {
    f: 1,
    a: 1,
    c: 1, 
    e: 1,
    b: 1,
    o: 2,
    k: 1
}

b_hist = {
    e: 1,
    c: 1
}
"""
        