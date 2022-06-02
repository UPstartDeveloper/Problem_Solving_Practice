from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        LeetCode: https://leetcode.com/problems/running-sum-of-1d-array/
        
        input:
            int[pos/neg, unsorted, len > 0, dupes]
            assume it's mutable
            
        Output: cumsum
        
        Intuition - for loop
        
        EC: 
            empty array - [0]
            anything out of range - ValueError
            
        [-9, -6,    0,   5, -3,  4, 4]
        [-9, -15, -15, -10, -7, -3  1]
            
        """
        sum_so_far = ssf = 0

        for index, num in enumerate(nums):

            ssf += num
            nums[index] = ssf

        return nums
