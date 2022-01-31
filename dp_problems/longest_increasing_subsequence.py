from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/longest-increasing-subsequence/
        Super thanks to Benyam Ephrem for explanation: https://www.youtube.com/watch?v=fV-TF4OvZpk
        
        Input/Prob:
            - int[] 
                - 1 or more elems
                - relative order immutable
                - pos/neg
                - dupes
                - unsorted 
                
            - SIS = strictly increasing subsequence
                
        Output:
            max(len(SIS))
            
        Intuition:
            dynamic programming
            binary search?
            longest SORTED subseq --> set() --> len()
            
        EC:
            ValueError:
                - invalid size
                - wrong dtype
                
            Special case:
                - min value is already at index 0 --> 1 pass?
        
        Approach:
            BCR = O(n log n)
            
            1) Brute Force - quadratic
                # A LIS = -inf
                # B: find LIS from each starting index - TODO
                    idea: l->r, count # of times value increases from before
                    # C: update LIS
                # D: return LIS
                
                Time: O(n^2) on desc order
                                                
                optimize - if LIS == len(nums), stop early!
                
            2) Recursive:
                subprob:
                    if this val > prev_val -> do I keep or not?
                        if yes --> increment LIS, prev_val
                        if not --> move on without it
                    if this val <= prev_val
                        continue
                    then take max() of all
                    
                Time: O(n * 2^n) (but might work for all EC)
                
            3) Binary Search + DP:
            
            A: find the longest sorted contiguous subarr
            
            B: for each subarr:
                use binary search on the left --> see if can add values < 1st arr_val
                use binary search on the right --> see if can add values > last val
                
            C: for each subseq --> linear search for the longest len:
                pass it to len(set())
                
            D: return the longest length!
            
            
            4) Optimal Approach:
            
                A: init an arr of 1's
                
                B: for each ndx from 2 --> n - 1:
                    
                    1) scan all the indicies from 0 --> ndx - 1 --> find max
                    2) compare max + 1 X current_ans --> update current_ans
                    
                C: return the max(arr)
            
            [0,1,0,3,2,3] <--- solve THAT edge case
                   ^
             
             LIS
             0, 1, 2   
        """
        ### HELPERS
        def _find_length_lis(index):
            # track current val, size of current subseq
            current_val = nums[index]
            sub_seq_size = sss = 1
            # traverse 
            ndx2 = index + 1
            while ndx2 < len(nums):
                val2 = nums[ndx2]
                # track everytime increase 
                if val2 > current_val:
                    current_val = val2
                    sss += 1 
                # move on
                ndx2 += 1
            # all done!
            return sss
        
        def _scan_prev_ans(index, sa):
            ''''finds the set of SIS lengths before the current index'''
            largest_length, prev_ndx, current_elem = 0, 0, nums[index]
            while prev_ndx < index:
                # double check this length can be included in the new subseq
                if nums[prev_ndx] < current_elem and largest_length < sa[prev_ndx]:
                    largest_length = sa[prev_ndx]
                # move on
                prev_ndx += 1
            # all done!
            return largest_length
        
        ### MAIN
        # A: init an arr of 1's
        sub_ans = sa = [1 for _ in range(len(nums))]
        # B: for each ndx from 2 --> n - 1:
        for index in range(1, len(sa)):
            # 1) scan all the indicies from 0 --> ndx - 1 --> find max
            prev_ans = _scan_prev_ans(index, sa)
            # 2) compare max + 1 X current_ans --> update current_ans
            current_ans = sa[index]
            sa[index] = max([current_ans, prev_ans + 1])
        # C: return the max(arr)
        return max(sa)
