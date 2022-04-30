from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        LeetCode: https://leetcode.com/problems/finding-3-digit-even-numbers/
        
        Input
            single digit int, 0 or pos
            
        Output:
            list of combos ---> sorted
            
        Intuition:
            backtracking
            sorting? 
            ***enumeration***
        
        EC:
            TODO
            
        Approach:
        
            1) Permutations
                current_perm = []
                choices = [2, 1, 3, 0]
                all_perms = []
                
            # A: find all the permutatios
            # B: filter by which meet the reqs
            # C: sort the list of "valid"
                
        
        """
        ### HELPERs
        def _as_int(current_perm):
            """assumes the input has >= 3 int elems"""
            return (100 * current_perm[0]) + (10 * current_perm[1]) + (current_perm[2])

        def _form_permutations(h, digits):
            all_perms = ap = list()
            # 1st loop: can be any nonzero digit
            for first in range(1, 10):
                # 2nd: can be any digit
                for second in range(10):
                    # 3rd: any even digit
                    for third in range(0, 10, 2):
                        permutation = p = [first, second, third]
                        # validate it: do we reuse the same element?
                        if Counter(p) <= h:
                            ap.append(p)
            return ap

        ### MAIN
        # A: tally value counts
        histogram = h = Counter(digits)  # O(n)
        # B: form permutations
        perms = _form_permutations(h, digits)  # O(1)
        # C: "encode" the perms as ints
        return [_as_int(perm) for perm in perms]  # O(1)
