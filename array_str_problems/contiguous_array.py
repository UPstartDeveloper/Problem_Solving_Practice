from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/contiguous-array/submissions/
        
        Input/Problem:
            int[0 or 1, immmutable, unsorted, dupes, non-empty]
            
            contiguous = subarray where elems adj
            
        Output:
            max(len(sub_arr_uniform))
            
        Intuition:
            DP
            
            valid = # no. of 1/0
            
        EC:
            - size constraint
            - non-binary
            - many repeated 
                [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1] - start at change, expand out
            - many interlaced
                [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] - start at change, expand fwd
            
        Stepping Stones:
        
        1. Subproblem - validate a subarray
            1. for loop - traverse subarr, compare counts 0 == 1  
            
        2. 
        
        Approach:
        
            1) Try out all the possibilites --> O(n^2)
                # A: form --> dupe work
                
                # B: validate them
                
                # C: return the len(longest)
            
                [0,1,0]
                 _
                 _ _
                 _ _ _
                   _ 
                   _ _
                     _
                [0]
                
            2) DP:
                
                A: map all even ints (0 --> len(num)) --> exp_ndx (int - 1) - O(N)
                
                B: traverse the dict - for each even int - O(n^2)
                    SKIP 0
                    go to its index ---> verifying it's valid
                    if not valid --> increment that ndx fwd, until it goes len(num)
                    
                C: traverse the dict - linear search for answer - - O(N)
                    if dict[length] ---> valid ndx --> it become new_highest length
                    
        
        """

        ### MAIN
        sub_sum_indices = {0: -1}
        max_length, sum_so_far = 0, 0
        for index, bit in enumerate(nums):
            if bit == 0:
                sum_so_far -= 1
            else:  # bit == 1
                sum_so_far += 1
            if sum_so_far in sub_sum_indices:
                # get the longest length possible, by seeing the first time this happened
                first_time = sub_sum_indices[sum_so_far]
                total_length = index - first_time
                max_length = max(max_length, total_length)
            else:  # first time seen
                sub_sum_indices[sum_so_far] = index
        return max_length
