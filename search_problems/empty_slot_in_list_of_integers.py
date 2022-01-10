from typing import List


class Solution:
    def find_missing(nums: List[int]) -> int:
        """
        InterviewQs Problem:
            You have a list of integers that range from values 1 to n. 
            Each value in the list is unique, 
            however one random slot in the list is empty, 
            making the size of the input array n-1. 

            Can you write a function to find the missing integer?
    
        Example:
            Input: arr[] = [1, 2, 4, 6, 3, 7, 8]
            Output: 5
            
            Input: arr[] = [1, 3, 2, 5, 6]
            Output: 4
            
        """
        # O(n) time, O(1) solution
        # A: insert a "null" value for the missing int
        nums.append(0)
        # B: find the index of the missing value
        index = 0
        while index < len(nums):
            # a: move the current value into its sorted position
            while not (nums[index] == index + 1 or nums[index] == 0):
                # i. "kick" this value to its sorted index in the arr
                if nums[index] > 0:
                    sorted_index = nums[index] - 1
                    nums[index], nums[sorted_index] = nums[sorted_index], nums[index]
            # b: move on
            index += 1
        # C: return the missing value
        return nums.index(0) + 1
