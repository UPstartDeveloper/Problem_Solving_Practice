class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
        
        Input/Problem
            str[can be empty, immutable, repeating]
            ASSUME case-sensitive
            ASSUME notice spaces
        
        Output:
            len(longest_sub_without_repeata)
            
        Intuition:
            hash map
            pointers
            
        EC:
            "" --> 0
            TODO
            
        Approach:
            1. Quadratic Solution w/ Hashmap
                - O(n^2), space O(n)
                - nested for loops
            
        """
        # EC:
        if s == "":
            return 0
        # Quadratic Solution
        longest = 1
        for index1 in range(len(s)):
            seen_before = set()
            # find the longest no-repeat substring
            for index2 in range(index1, len(s)):
                if s[index2] in seen_before:
                    break
                else:
                    seen_before.add(s[index2])
            # update the longest length, if appropiate
            longest = max(longest, len(seen_before))
            
        return longest
