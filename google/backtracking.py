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


class Solution:
    def combine_unique(
        self, nums: List[int], target_size: int
    ) -> List[List[int]]:
        """
        Given a collection of numbers, nums, that might contain duplicates, 
        returns all possible unique combinations.

        LeetCode: https://leetcode.com/problems/permutations-ii/
        """
        
        ### HELPERS
        def _recursor(current, all_p, choices) -> set:
            # base
            if len(current) == target_size:
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
                    if index > other_ndx
                ]
                _recursor(current, all_p, rems)
                current.pop()
            return all_p
            
        
        ### DRIVER
        # EC: target_size == n
        if len(nums) == target_size:
            return [nums]

        # general algo
        all_p = _recursor(list(), set(), nums) 
        return list([list(p) for p in all_p])


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given a collection of numbers, nums, that might contain duplicates, 
        returns all possible unique subsets of integers.
        """
        
        ### HELPERS
        def _recursor(current, all_sub, choices, target_size) -> set:
            # base
            if len(current) == target_size:
                # add as a tuple to a set
                current = tuple(current[:])
                # check for dupes
                if current not in all_sub:
                    all_sub.add(current)
                return
            # recursive
            for index, number in enumerate(choices):
                current.append(number)
                rems = [
                    val 
                    for other_ndx, val in enumerate(choices)
                    if index > other_ndx
                ]
                _recursor(current, all_sub, rems, target_size)
                current.pop()
            return all_sub
            
        
        ### DRIVER
        # EC: target_size == n
        if len(nums) == 1:
            return [nums]

        # general algo
        all_sub = list()

        for size in range(1, len(nums)):
            sub = _recursor(list(), set(), nums, size) 
            all_sub.extend(list([list(s) for s in sub]))

        return all_sub
