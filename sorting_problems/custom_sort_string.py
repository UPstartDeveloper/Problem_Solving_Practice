from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Leetcode: https://leetcode.com/problems/custom-sort-string/
        
        Input/Problem
            2 non empty strings
            only English - lowercase

            order = set of chars
                chars in s NOT in order
                chars in order NOT in s

            only common char(c, order) they need same relative order in perm

        Output: 1 permuted string
        
        Intuition:
            order = set of chars
            dynamic
            sort
            
        EC:
            invalid chars
            empty str
            
            
        Approach:
            DIY
                         01234
                order = "cbafg", s = "abcd"
                
                ordering_values = 0     1       2       3       4.    5
                                  c.    b.      a.      f.      g.    d
                
                char_freq_in_s = {
                    a: 1,
                    b: 1, 
                    c: 12,
                    d: 1
                }
                
                output = "c"
        """
        ### HELPERS
        def _make_ordering_values(order, s):
            ordering_values, char_set = list(order), set(order)
            for char in s:
                if char not in char_set:
                    ordering_values.append(char)
                    char_set.add(char)
            return ordering_values

        def _new_string(ordering_values, char_freq_in_s):
            new_str_chars = list()
            for index, unique_char in enumerate(ordering_values):
                count = char_freq_in_s[unique_char]
                for _ in range(count):
                    new_str_chars.append(unique_char)
            return "".join(new_str_chars)

        ### DRIVER
        # A: make an order for all the chars
        ordering_values = _make_ordering_values(order, s)
        # B: frequency dist of s
        char_freq_in_s = Counter(list(s))
        # C: make the new string
        return _new_string(ordering_values, char_freq_in_s)
