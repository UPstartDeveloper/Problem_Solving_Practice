from typing import List


class Solution:        
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        """
        Leetcode: https://leetcode.com/problems/largest-sum-of-averages/
        
        Input/Problem:
            ASSUME nums is immutable
            non empty
            pos ints
            length >= k >= 1
            unsorted
            dupes
            
        Output:
            max(score)
            multiple partitions
            
        Intuition:
            max (score) ---> make smaller partitions for the larger numbers
            
        EC:
        `  - TODO
        
        Approach:
        
            1. Heaps
            
            2. Brute:
                A: find all possible partitions (by lengths)
                B: for each
                    compute score avgs of each subarr
                C: take the max 
                
        """
        ### HELPERS
        def _backtracking_helper(all_ways, total, num_parts, current_way):
            # Base: 
            if len(current_way) == k and sum(current_way) == len(nums):
                all_ways.add(tuple(current_way[:]))
            # Recursive: keep finding more values
            else:
                # find the "bounds" on how long this next partition can be
                nums_so_far = sum(current_way)
                partitions_left = num_parts - 1
                highest_possible_len = total - (partitions_left * 1)
                # explore the entire space of possibilities
                for partition_len in range(1, highest_possible_len + 1):
                    # update the current partition
                    current_way.append(partition_len)
                    # recurse
                    nums_remaining = total - partition_len
                    _backtracking_helper(all_ways, nums_remaining, 
                                         partitions_left, current_way)
                    # "backtrack" for next iteration
                    current_way.pop()
            # all done!
            return all_ways
                    
        def _compute_all_schemes(total, num_parts):
            """finds all the ways to add k positive ints up to total"""
            all_ways = set()
            return _backtracking_helper(all_ways, total, num_parts, [])
        
        def _compute_score(nums, scheme):
            """given a list of how long to make each subarr --> compute score"""
            sums, nums_index, scheme_index = list(), 0, 0
            # for each subarray - compute its sum
            while scheme_index < len(scheme):
                next_part = scheme[scheme_index]
                sums.append(sum(nums[nums_index:nums_index + next_part]))
                nums_index += next_part
                scheme_index += 1
            # return overall score
            return sum([sum_val / length for sum_val, length in zip(sums, scheme)])
                
        ### MAIN
        self.max_score = 0
        # A: find all possible partitions (by lengths)
        partition_schemes = _compute_all_schemes(len(nums), k)  # TODO[code]
        print(partition_schemes)
        # B: for each
        for scheme in partition_schemes:
            # compute score avgs of each subarr, and update output
            score = _compute_score(nums, scheme)  # TODO[code]
            self.max_score = max(self.max_score, score)
        # C: take the max 
        return self.max_score
        
        
