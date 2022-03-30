from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        LeetCode: https://leetcode.com/problems/find-the-duplicate-number/
        
        Input:
            nums: int[> 0, unsorted, un-empty]
            n = largest # in nums
            1 dupe
            
        Output:
            dupe int
            
        Intuition:
            nested for loop - O(n^2)
            
            sorting, hashset - N/A
            
            How can we prove that >=1 duplicate number must exist?
            n = max(nums) >= # unique elems
            len(nums) - # unique elems = # duplicates 
            len(nums) - n = # duplicates 
            (n + 1) - n = # duplicates > 0
                        = # duplicates >= 1
                        
            Can you solve the problem in linear runtime complexity?
            
            5 - 4 = 1
            
            [1, 2, 3, 4, 5] = 15
            [1, 3, 4, 2, 2] = 12
        
        """
        ### HELPERS
        def _search_for_duplicate(nums) -> int:
            for index1 in range(len(nums)):
                for index2 in range(len(nums)):
                    if index1 != index2 and nums[index1] == nums[index2]:
                        return nums[index1]
            # edge case: no duplicates
            return 0
        
        def _search_for_duplicate_linear(nums) -> int:
            "solution for special case where # unique = n"
            largest = n = max(nums)
            sum_of_unique = sum(range(1, n + 1))
            sum_of_duplicates = sum(nums) - sum_of_unique
            num_of_duplicates = len(nums) - n
            return sum_of_duplicates // num_of_duplicates
        
        ### DRIVER
        # A: Brute force: check all pairs of numbers
        return _search_for_duplicate(nums)
        # B: optimized approach
        # return _search_for_duplicate_linear(nums)
    
"""
[3,1,3,4,2]
 1
     2
collections - sets, lists, dictionaries, heaps
constant extra space - fixed size array, pointers

"""
        
