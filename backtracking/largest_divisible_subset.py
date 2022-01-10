from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Leetcode: https://leetcode.com/problems/largest-divisible-subset
        
        Input/Problem:
            - non empty arr[int > 0]
            - immutable
            - unique
            - maybe sorted
            
            - Output:
                a subset where all pairs of nums are divisible
                --> optimize len(subset)
        
        Intuition:
            subset - recursive 
            dynamic programming
            
        EC:
            1) no solutions ---> return []
            2) invalid input ---> ValueError
            3) TODO
            
        Approach:
        
            1) Brute Force: backtracking
                A: compute all subsets 
                B: check all subsets - starting from largest
                    a) if divisible --> return subset
                C: return []
                
            2) DIY:
            
            nums = [1,2,3]
                   [3, 2, 1]
                       ^
                          ^
            
        """
        ### HELPERS
        def _compute_combinations(current_sub, all_subsets, subset_size, ndx=0):
            """TODO[test]: recursive backtracking"""
            # current sub is finished
            if len(current_sub) == subset_size:
                all_subsets.append(current_sub[:])
            else:  # recursive
                for index in range(ndx, len(nums)):
                    elem = nums[index]
                    current_sub.append(elem)
                    _compute_combinations(
                        current_sub, all_subsets, subset_size, ndx=index + 1
                    )
                    current_sub.pop()
            return all_subsets

        def _compute_subsets(nums):
            subsets = list()
            for subset_size in range(len(nums) + 1, -1, -1):
                subsets.extend(_compute_combinations([], [], subset_size))
            return subsets

        def _is_divisible(subset):
            for index1 in range(len(subset)):
                for index2 in range(len(subset)):
                    # fail fast
                    if (
                        subset[index1] % subset[index2] > 0
                        and subset[index2] % subset[index1] > 0
                    ):
                        return False
            return True

        ### DRIVER
        # A: compute all subsets
        subsets = _compute_subsets(nums)
        # B: check all subsets - starting from largest
        for s in subsets:
            # a) if divisible --> return subset
            if _is_divisible(s):  # TODO
                return s
