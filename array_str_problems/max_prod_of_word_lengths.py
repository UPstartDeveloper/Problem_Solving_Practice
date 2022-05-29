import heapq
from typing import List, Set, Tuple


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        LeetCode: https://leetcode.com/problems/maximum-product-of-word-lengths/
        
        Input:
            words: str[len > 0, lower Eng, ].len > 0
                immutable
            
        Output:
            max(prod(str1.len, str2.len), 0)
            str1 and str2 --> no common letters at all
            
        Intuition:
            disjoint set
            heaps
            
        EC:
            [], or [""] --> 0
            invalid chars --> ValueError
            
        Stepping Stone Problem:
            1) find two strs whose length prod --> max
                A: sort the arr by length of string
                B: multiply the last two lengths
            
            2) 1), but now we have to abide by the unique chars
            
        Approach:
            
            1) Brute Force -> O(n^2 * m) TODO[confirm]
                A: try every pair (for each str, do a lin_search)
                B: throw out any invalid
                C: return the longest, or 0
            
            2) Better:
                A: replace all str w/ letter_set + length - O(n)
                B: make disjoint set + max lens - O(n^2)
                C: heapsort - to get 2 largest - O(log(n))
                D: return prod, or only 1
                
        """
        ### HELPERS
        def _preprocess(words) -> List[Tuple[Set, int]]:
            return [
                (set(word), len(word))
                for word in words
            ]
            
        def _make_buckets(word_sets_and_len):
            # track all sets so far
            all_sets = list()
            # map each set to the largest length seen so far
            largest_per_set = dict()  # index -> lenght
            
            for word_index, word_obj in enumerate(word_sets_and_len):
                letter_set, length = word_obj
                # find the right bucket for this word
                bucket_idx = 0
                while bucket_idx < len(all_sets):
                    current_set = all_sets[bucket_idx]
                    # check for "overlap"
                    # TODO
                # once found - map the bucket_index -> length
                
        ### DRIVER - brute force - O(w^2 * l) time, O(w * l) space,
        #              where w = # of words, and l = longest length
        # A)
        word_sets_and_len = _preprocess(words)
        # B) find the highest prod
        max_prod, empty_set = 0, set()
        for set1, len1 in word_sets_and_len:
            for set2, len2 in word_sets_and_len:
                # throw out all the invalid
                if len(set1.union(set2)) == len(set1) + len(set2):
                    # set the max_prod
                    max_prod = max(max_prod, len1*len2)
        # C)
        return max_prod
