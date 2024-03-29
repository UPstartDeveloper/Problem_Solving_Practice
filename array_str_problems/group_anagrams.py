from typing import List


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
        """
        Solution 1: O(n^2 * l), where n = # strings and l = length of longest
                    O(n * l) space
        def make_histogram(string) -> dict:
            '''enumerate the tokens of each unique letter appears'''
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
            # D: check to make sure both has the same types and tokens
            for char, tokens in new.items():
                # try and get the character type from the other histogram
                if char not in old:
                    return False
                elif (char in old and tokens != old[char]):
                    return False
            return True
        # A: init a list for the output
        output = list()  # O(s)
        str_hists = dict()
        # B: loop over each string
        for new_string in strs:
            # search all the groups with a histogram of the string
            str_hist = make_histogram(new_string)
            # C: check if this string is an anagram in one of the groups
            for index, group in enumerate(output):
                if is_anagram(str_hist, str_hists[group[0]]) is True:
                    output[index].append(new_string)
                    break
             # D: if it's not, start a new group with it - [string]
            else:
                output.append(list([new_string]))
                str_hists[new_string] = str_hist
        #: E: return all the output as a 2D list
        return output
        """

        def alphabetize(strs):
            """sort the letters in each string, then as a whole"""
            # A: sort the letters in each individual string
            sorted_strs = list()
            for original_string in strs:
                str_list = list(original_string)
                str_list.sort()  # l log (l)
                sorted_str = "".join(str_list)
                sorted_strs.append((sorted_str, original_string))
            # B: sort the whole array of sorted strings
            sorted_strs.sort()
            print(sorted_strs)
            return sorted_strs

        # A: sort the letters in each individual string
        # B: sort the sorted strings relative to each other,
        sorted_strs = alphabetize(strs)
        # C: see which strings belong together
        groups = list()
        idx = 0
        while idx < len(strs):
            # find the string to match for this group
            group_string, original_string = sorted_strs[idx]
            # start a new group
            group = [original_string]
            # see how many strings fall in this group
            next_idx = idx + 1
            while next_idx < len(strs):
                if sorted_strs[next_idx][0] == group_string:
                    # add the string to the group,
                    group.append(sorted_strs[next_idx][1])
                    # move ahead in the array
                    next_idx += 1
                else:
                    break
            # update the index
            idx = next_idx
            # add the group to the output
            groups.append(group)
        # return the groups
        return groups


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


Pseudocode for another Solution, possibly linear time:

A: init two pointers at the first two strs
B: check which strings belong together:
    - if two words are anagrams:
        - place them in the first string's group (create if not already there)
        - then move both pointers ahead by one
    - otherwise:
        - make a new group for the second string
        - move ahead the second pointer only
C: return the groups

Example where this algorithm seemed to work:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
                1     2 MATCH
                      1     2 !MATCH
                      1           2 MATCH
                            1           2 MATCH
                                  1           2 !MATCH
Resulting output:
[["bat"],["nat","tan"],["ate","eat","tea"]]
                    
Actual Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
