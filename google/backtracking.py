from typing import List


class Solution:
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        """
        Given a collection of numbers, nums, that might contain duplicates, 
        returns all possible unique permutations in any order.

        LeetCode: https://leetcode.com/problems/permutations-ii/
        """
        
        ### HELPERS
        def _recursor(current, all_p, choices) -> set:
            # base
            if len(current) == len(nums):
                # add as a tuple to a set
                current = tuple(current[:])
                # check for dupes
                if current not in all_p:
                    all_p.add(current)
                return
            # recursive
            for index, number in enumerate(choices):
                current.append(number)
                rems = [
                    val 
                    for other_ndx, val in enumerate(choices)
                    if index != other_ndx
                ]
                _recursor(current, all_p, rems)
                current.pop()
            return all_p
            
        
        ### DRIVER
        all_p = _recursor(list(), set(), nums) 
        return list([list(p) for p in all_p])
        