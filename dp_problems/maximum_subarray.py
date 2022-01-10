from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/maximum-subarray/
        
        Blog post explanation (by MS alum Jessica Trinh): 
            https://levelup.gitconnected.com/kadanes-algorithm-solving-for-maximum-subarray-in-o-n-time-and-o-1-space-776290910090
        
        Problem Statement
        "Given an integer array nums, find the contiguous subarray
        (containing at least one number) which has the largest sum and return its sum."
        - pos/neg
        - dupes
        - unsorted

        - no []

        1. Brute force
        Intution: try all permutations

        Approach:
        largest_sum = -2


        [-2,1,-3,4,-1,2,1,-5,4]
            s
               e

        # first for loop - keeps track of the start
        # nested for loop - decides the end of the subarray
        # nested - calculate the sub_sum

        Edge Cases:
        1) [] ---> error
        2) single positive [-5,-4,1,-7,-8] ==> return max of list

        2. DP

        [-2,1,-3,4,-1,2,1,-5,4]
          s
               e
        localSum = -2, -1, -2, -3
                   -3, 1, 0 ----> sum of s and e pointers
        globalSum - largest sub_sum
                  = -1
                  = 1,

        # A: localSum --> summing between s and e
        # B: lS > gS
        # C: if True:
                update gS, move e ahead
             but if False:


        Ideas:
        1. when sum(s, e) < localSum ---> move s to e
        2. when sum(s, e) < localSum ---> move s one step at a time to e
        3.

        [5,4,-1,7,8]
         ^      ^

         ------------------------------------------------------
         Better DP solution
         Subproblems:
         1. finding starting subarray position
            - don't start it on a negative - if all negatives,
                return max()

         2. summing a cont. subarray
            - keep a running localSum,
              update it with the next value

         3. identifying the best subarray
            - anytime the next value makes the sum less, the
                the subarray must end
                - is localSum drops negative --> 0
            - always compare localSum and globalSum

        Why does this work?
            - we keep adding values to localSum that make it larger, even if temporarily it goes less
            - but we still are able to find globalSum when we need to
            - quickly updating the localSum
            - EDGE CASE: make the solution work for when all negatives, by initializing out to -inf
        --------------------------------------------------------
        """
        # A: init ouput
        global_max = float("-inf")
        # B: find the useful localSums
        local_sum = 0
        for index, value in enumerate(nums):
            # update local sum
            local_sum += value

            # see if we found global sum
            global_max = max(local_sum, global_max)

            # restart local_sum if needed
            if local_sum < 0:
                local_sum = 0

        # C: return output
        return global_max
