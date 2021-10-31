from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/h-index/submissions/

        Input/Problem:
            - h = possibly one of citations indices
            - ASSUME h-index is possible
            - h-index is >= 0
            - at least 1 citation
            - Input:
                - unsorted arr
                - immutable
                - dupes poss
                - non negatives
                - non empty

        EC:
            1) malformed input ([], negs)
                - ValueError

        Definition:
            h-index: value such that:
                 if h values >= least h
                 and
                 if (n − h values) = l <= h.
                    3 - 1
                    2 values <= 1

        Intuition:
            - max possible h-index
            - don't reuse values for both conditions

        [1,3,1]

        Possible h      :               0 1 2. 3
        # Valeues >= h:                 0 1
        Actual # Values >= h:             1
        Exp. # Values <= h:               2
        Actual # Values <= h:             2


        [3,0,6,1,5]
         ^
        Possible h:                  0 1 2. 3
        # Valeues >= h (exp):               3
        Actual # Values >= h:               3
         # Values <= h (exp):               2
        Actual # Values <= h:               2

        Approach:

            1) Matrix - (n + 1) x (4)
            DRIVER
                A: 0 matrix of (n + 1) array
                B: fill in the cols [TODO] - T/F if that index is h-index
                C: traverse from high to low:
                    D: check if it's an h-index
                    E: if so, then return it

            HELPERS
            1) fill_in:
                traverse the indices:
                    h = index
                    calculate expectations = h and n - h
                        exp_num_greater_or_eq = h
                        exp_num_less_or_eq = n - h
                    calculate the actuals:
                        actual_num_greater = 0
                        actual_num_less = 0
                        traverse the array
                            increment the appropiate actual_var (only up to exp)
                    return bool based on:
                        1) actual_num_greater + actual_num_less = n
                        2) actual_num_greater == exp_num_greater_or_eq
                        3) actual_num_less == exp_num_less_or_eq

        """
        ### HELPERS
        def _count_sort(nums):
            """TODO: make this sort from greatest to least!!"""
            # A: def sorting params
            min_val, max_val = min(nums), max(nums)
            multiset = [0 for _ in range(max_val - min_val + 1)]
            # B: see how many there are of each unique int
            for n in nums:
                index = n - min_val
                multiset[index] += 1
            # C: create a sorted version of the input
            sorted_nums = []
            for index, value_count in enumerate(multiset):
                value_type = index + min_val
                for _ in range(value_count):
                    sorted_nums.append(value_type)
            # D: all done!
            return sorted_nums

        def _is_h_index(h, citations):
            # calculate expectations = h and n - h
            exp_num_greater_or_eq = h
            exp_num_less_or_eq = len(citations) - h
            # calculate the actuals:
            actual_num_greater = ang = 0
            actual_num_less = 0
            # traverse the array
            for c in citations:
                # increment the appropiate actual_var (only up to exp)
                if c >= h and ang < exp_num_greater_or_eq:
                    ang += 1
                elif c <= h and actual_num_less < exp_num_less_or_eq:
                    actual_num_less += 1
            return (
                (ang + actual_num_less) == len(citations)
                and ang == exp_num_greater_or_eq
                and actual_num_less == exp_num_less_or_eq
            )

        ### DRIVER
        # TODO: after modifying the _count_sort func above, remove the call to reversed() here!!!
        sorted_citations = reversed(_count_sort(citations))
        # Try All Possibles
        for index in range(len(citations) + 1, -1, -1):
            # D: check if it's an h-index
            if _is_h_index(index, sorted_citations) is True:
                return index
        return -1  # should never run
