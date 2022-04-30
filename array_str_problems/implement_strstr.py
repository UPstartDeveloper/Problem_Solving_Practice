class Solution:
    """LeetCode: https://leetcode.com/problems/implement-strstr/"""
    def strStr(self, haystack: str, needle: str) -> int:
        # init runner
        index_hay = ih = 0
        
        # find the occurence
        occurence = -1
        while ih < len(haystack):
            if haystack[ih] == needle[0]:
                # validate if this contains the entire needle
                hay_index = hi = ih + 1
                needle_index = ni = 1
                while (
                    hi < len(haystack) and
                    ni < len(needle) and
                    haystack[hi] == needle[ni]
                ):
                    hi += 1
                    ni += 1
                # needle is found!
                if ni == len(needle):
                    occurence = ih
                    break
            # move on
            ih += 1
            
            
        # all done
        return occurence
        
