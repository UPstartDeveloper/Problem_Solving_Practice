class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Leetcode Link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

        Input/Problem:
            - ASSUME non empty
            - pos ints
            - subarrays --> sums --> # of odd sums
            - ASSUME input immutable
            - ASSUME input can have dupes
            - ASSUME input may not be sorted
            - ASSUME # of subsets can still fit in RAM
            Output:
            - return num_odd_sums % (10**9 + 7)

        rules:
            O + O = E
            E + E = E
            O + E = O

        EC:
            1) empty array --> ValueError?
            2) non-pos --> ValueError?

        Intuition:
            subset

        Approach:

            1) Recursive Backtracking - for combos, not perms

            # A: find all subarrays
            # B: find all sums
                # C: counting if it's oddd
            # D: return the count

        """
        ### HELPER
        def _count_odd_sums_going_from(index):
            odd_sums, accu_sum = 0, 0
            while index < len(arr):
                accu_sum += arr[index]
                if accu_sum % 2 > 0:
                    odd_sums += 1
                index += 1
            return odd_sums

        ### DRIVER
        # A: init total_count
        total_count = 0
        # B: find all subarrs
        for index in range(len(arr)):
            # C: use DP to increment whenever it's an odd sum
            total_count += _count_odd_sums_going_from(index)
        # D: return total_count
        return total_count % (10 ** 9 + 7)
        """
        ### HELPERS
        def _get_remaining(choices, index):
            return [
                value for next_index, value in enumerate(choices)
                if next_index > index
            ]
        
        def _generate_combos(current_combo, all_combos, size, choices):
            # Base Case:
            if len(current_combo) == size:
                all_combos.append(tuple(current_combo[:]))
            # Recursive: keep filling up the subset
            else:
                for index in range(len(choices)):
                    value = choices[index]
                    current_combo.append(value)
                    rems = _get_remaining(choices, index)
                    # recurse
                    _generate_combos(current_combo, all_combos, size, rems)
                    # after popping, remove last added
                    current_combo.pop()
            return all_combos
        
        def _generate_subs(choices):
            # A: init a subsets array
            all_subsets = list()
            # B: iterate over each subset size we care about
            for size in range(1, len(choices) + 1):
                # find all combos of that size
                combos = _generate_combos([], [], size, choices)
                all_subsets.extend(set(combos))
            # C: all done!
            return all_subsets
        
        ### DRIVER
        # A: find all subarrays
        subarrs = _generate_subs(arr)
        # B: find all sums 
        odds = 0
        for sub in subarrs:
            if sum(sub) % 2 > 0:
                odds += 1
        # C: counting if it's odd
        return odds
        """


"""
numOfSubarrays
arr                 subarrs
[1, 3, 5]           TBD
--------------------
_generate_subs

all_subsets         size        combos
[
[1], [3], [5]
]                    1             TBD
--------------------
_generate_combos

current_combo, size,  choices                all_combos
[]                1     [1, 3, 5]              [[1],] 
    
index        value      rems
0              1        [3, 5]
1

"""
