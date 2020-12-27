class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Problem:
        - each string has at least 1 char
        - string chars are lower case English chars only
        - there is guaranteed to be 0 or more strings
        
        Questions:
        - can there be duplicate strings? no
        
        
        edge case:
        [[]] -> [[]]
        [] -> ValueError
        
        Brainstorm:
        
        test input
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        Idea 1: Brute force iterate, compare
        # intuition: check if each string falls in a predefined group of anagrams,
                     and if not start a new group of anagrams
        # approach:
        
        # A: init a list for the output
        # B: loop over each string
            # C: check if this string is an anagram with 1 str from all of the other groups
            # D: if it's not, start a new group with it - [string]
        #: E: return all the output as a 2D list

        
        """
        def make_histogram(string) -> dict:
            '''enumerate the number of times each unique letter appears'''
            hist = dict()
            for char in string:
                if char in hist:
                    hist[char] += 1
                else:  # char not in hist
                    hist[char] = 1
            return hist
        def is_anagram(new, old) -> bool:
            # B: check the lengths of the strings
            if len(new) != len(old):
                return False
            # C: make histograms for both strings
            new_hist, old_hist = (
                make_histogram(new), make_histogram(old)
            )
            # D: check to make sure both has the same types and tokens
            for char, tokens in new_hist.items():
                # try and get the character type from the other histogram
                if char not in old_hist or (char in old_hist and tokens != old_hist[char]):
                    return False
            return True
        # A: init a list for the output
        output = list()  # O(s)
        # B: loop over each string
        for new_string in strs:
            group_index = -1
            # C: check if this string is an anagram with 1 str from all of the other groups
            for index, group in enumerate(output):
                if is_anagram(new_string, group[0]) is True:
                    group_index = index
            # D: if it's not, start a new group with it - [string]
            if group_index > -1:
                output[group_index].append(new_string)
            else:
                output.append(list([new_string]))
        #: E: return all the output as a 2D list
        return output
    
"""
output = [
["eat", "tea", "ate"],
["tan", "nat"],
["bat"]
]

strs = 
["eat","tea","tan","ate","nat","bat"]

ns =        index   group
"eat"       
"tea"       0       ["eat"]
"tan"       0       ["eat", "tea"]
"ate"       0       ["eat", "tea"]
"nat"       0       ["eat", "tea", "ate"]
            1       ["tan"]
"bat"       0

new = "nat"
old = "tan"

Time: O(s^2) when each s belongs in it's own group
Space: O(s + l), where l = is the length of the longest string
"""
