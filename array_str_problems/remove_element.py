from typing import List

class Solution:
    """Leetcode: https://leetcode.com/problems/remove-element/"""
    def removeElement(self, nums: List[int], val: int) -> int:
        # A: set init positions
        index1, index2 = 0, len(nums) - 1
        # B: make swaps
        while index1 < index2:
            # move pointers
            while index1 < len(nums) and nums[index1] != val:
                index1 += 1
            while index2 > -1 and nums[index2] == val:
                index2 -= 1
            # swap
            if 0 <= index1 < len(nums) and 0 <= index2 < len(nums):
                # ensure the swaps goes in the right direction
                if index1 < index2:
                    nums[index1], nums[index2] = nums[index2], nums[index1]
                index1 += 1
                index2 -= 1
        # C: count non-vals
        final_ndx = 0
        while final_ndx < len(nums):
            if nums[final_ndx] == val:
                break
            final_ndx += 1
        return final_ndx
            
        
