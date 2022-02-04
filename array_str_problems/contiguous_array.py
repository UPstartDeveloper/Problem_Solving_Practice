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
        def _is_valid(answer_ndx, even_length):
            if -1 < answer_ndx < len(nums):
                sub_arr_sum = sum(nums[answer_ndx - even_length + 1:answer_ndx + 1])
                return sub_arr_sum == even_length / 2
            return False
            
        def _map_possible_answers(total_length):
            """map all even ints (0 --> len(num)) --> exp_ndx (int - 1) - O(N)"""
            possible_valid_lengths = {0: 0}
            for even_length in range(2, len(nums) + 1, 2):
                possible_valid_lengths[even_length] = even_length - 1
            return possible_valid_lengths
        
        def _verify_lengths(nums, possible_valid_lengths):
            for even_length in range(2, len(nums) + 1, 2):
                # go to its index ---> verifying it's valid
                answer_ndx = possible_valid_lengths[even_length]
                while answer_ndx < len(nums) and _is_valid(answer_ndx, even_length) is False:
                    answer_ndx += 1
                possible_valid_lengths[even_length] = answer_ndx
        
        ### MAIN
        # A: id potential answers
        possible_valid_lengths = _map_possible_answers(len(nums))
        # B: traverse the dict - for each even int - O(n^2)
        _verify_lengths(nums, possible_valid_lengths)
        # C: traverse the dict - linear search for answer - - O(N)
        final_answers = [
            length for length, index in possible_valid_lengths.items()
            if -1 < index < len(nums)
        ]
        return max(final_answers)
