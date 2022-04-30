from collections import Counter


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        LeetCode: https://leetcode.com/problems/valid-palindrome-ii/
        
        Input:
            s: str - non-empty, lowercase, immutable
            
        Output:
            bool
                true if palindro OR 1 off
                
        Intuition:
            linear pass - 2 pters
            
        EC:
            
        
        "abca" exp_num = 2, actual =  1
          ^^
         
         aba - true
         
         aca - true
        
        "abc" exp_num = 2, actual =  1
           ^
         ^
          
        Approach:
        
            1) Linear pass
            
                length of str ---> exp # of matches --> ceil(len() / 2)
                1 pass: actual # of passes
                
            2) Brute force: 
                Counter(char -> # occurences)
                    valid -> odd + only 1 letter appears an odd # of times
                             even + only 2 letters appears an odd # of t,
                             even + all letters appear an even # of ti
                             
            3) Linear Pass AND Rules
                A: # of mismatches
                B: if # == 0 --> True
                C: if # == 1 --> True IF one of the mismatching cahrs at the mid
                
        
        """
        ### HELPER
        def _check_palindrome(p1, p2):
            while p1 < p2:
                if s[p1] != s[p2]:
                    # invalid indices = NOT a palidrome
                    return -2, -2
                p1 += 1
                p2 -= 1
            return p1, p2

        ### DRIVER
        # A: try to validate the whole string
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            # A1: if mismatch, try to see if a deletion fixes it
            if s[p1] != s[p2]:
                is_palindrome_without_p2 = _check_palindrome(p1, p2 - 1)
                is_pal_without_p1 = _check_palindrome(p1 + 1, p2)
                # A2: invalid string found
                if (-2 in is_palindrome_without_p2) and (-2 in is_pal_without_p1):
                    return False
                # A3: string still works, let's move on (w/ no duplicate checks)
                elif -2 not in is_palindrome_without_p2:
                    p1, p2 = is_palindrome_without_p2
                else:
                    p1, p2 = is_pal_without_p1
            # A4: no issue, move on
            else:
                p1 += 1
                p2 -= 1
        # B: all done!
        return True
