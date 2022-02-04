from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
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
        ### HELPERS
        def get_valid_length(sub):
            if (
                len(sub) % 2 == 0 and 
                sum(sub) == (len(sub) / 2)
            ):
                return len(sub)
            else:
                return 0
            
        def _generate_sub(start):
            """continually 'extend' from the starting index"""
            subs_from_start = list()
            sub_so_far = list()
            for index in range(start, len(nums)):
                sub_so_far.append(nums[index])
                subs_from_start.append(sub_so_far[:])
            return subs_from_start
        
        def _create_subarrays(nums):
            subs = list()
            for start in range(len(nums)):
                subs.extend(_generate_sub(start))
            return subs
        
        ### MAIN
        # A: form --> dupe work
        all_subs = _create_subarrays(nums)  #O(n^2)
        # B: validate them
        valid_subs = [get_valid_length(sub) for sub in all_subs]  # O(n^3)
        # C: return the len(longest)
        return max(valid_subs)  # O(n^2)
