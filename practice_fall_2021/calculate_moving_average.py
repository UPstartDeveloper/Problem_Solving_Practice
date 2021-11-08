from typing import List

class Solution:
    def calculate_moving_averages(nums: List[int], p) -> List[int]:
        """
        From InterviewQs:
        
        You are given a list of numbers and a single number p.  
        Write a function to return the minimum and maximum averages 
        of the sequences of p numbers in the list.

        For example:
            # Array of numbers
            J = [4, 4, 4, 9, 10, 11, 12]
                    ^     ^
            # Length of sequences, p 
            p = 3

        Here, the sequences will be:  
            (4,4,4) 
            (4,4,9)  
            (4,9,10)    
            (9,10,11)  
            (10,11,12)  

        From the above we can see that:
            the minimum average will be 4 and 
            the maximum average will be 11, 
        which corresponds to the first and last sequences.
        """
        # A: Check edge cases:
        if p > len(nums) or p < 0:
            raise ValueError(f"There is no sequence with {p} values in {nums}")
        # B: init the outputs
        current_sum = sum(nums[:p])
        min_avg = max_avg = (current_sum / p)
        # C: calculate the averages over other sequences
        index1, index2 = 1, p
        while index1 < len(nums) and index2 < len(nums):
            # compute the new avg
            new_sum = current_sum + nums[index2] - nums[index1 - 1]
            new_avg = new_sum / p
            # update min and max as needed 
            if new_avg < min_avg:
                min_avg = new_avg
            elif new_avg > max_avg:
                max_avg = new_avg
            # move on to the next sequence
            current_sum = new_sum
            index1 += 1
            index2 += 1
        # D: all done!
        return [min_avg, max_avg]

"""
 0  1  2  3   4   5   6
[4, 4, 4, 9, 10, 11, 12], p = 3
                  ^       ^
cs = 12, 17
max = 4
min = 4, 5.6

i1 = 1, 2
i2 = 3, 4

ns = 12 + 9 - 4 = 17
na = 17 / 3 = 5.6


[4, 4, 4, 9, 10, 11, 12], p = 7

"""


