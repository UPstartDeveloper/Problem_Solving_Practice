from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        LeetCode: 
            https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
            
        Input:
            int[sorted, pos/neg, prev >= next, ]
            target - maybe in arr
            
        Output:
            bounds on that elem's subarray
            
        Intuition:
            binary search
            NOT trees
            
        EC:
            - [] ---> [-1, -1]
            - [-1 , -1]
            - invalid
            
        Approach:
        
            1) Brute force: linear search
                - while 
                    take inedex of frist === target
                    when elem !== target ---> take the last index we looked at
                    
            2)  Binary Search:
                - starting == ending
                    - normal D&C
                
                - starting != ending
                    - normal D&C
                    - two pointer <-->  ----> O(n)
                           < >
                    [5,7,7,8,8,10]
                         ^   ^
                         
                    [8,8,8,8,8,8,8,8,8,8,8,8]
                     ^   ^     ^
                         
            3) Binary Search Maybe
                - A: search for proximal values < and > target
                
            4) 
        
        """
        ### HELPERS
        def _search_start(target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_elem = me = nums[mid]
                # base case: answer found
                if me == target:
                    # did we find the first?
                    if (mid == 0) or (mid > 0 and nums[mid - 1] != target):
                        return mid
                # recursive: go left
                if target <= me:
                    hi = mid - 1
                # recursive: go right
                else:  # target > me
                    lo = mid + 1

            # not found
            return -1

        def _search_ending(target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_elem = me = nums[mid]
                # base case: answer found
                if me == target:
                    # did we find the first?
                    if (mid == len(nums) - 1) or (
                        mid < len(nums) - 1 and nums[mid + 1] != target
                    ):
                        return mid
                # recursive: go left
                if target < me:
                    hi = mid - 1
                # recursive: go right
                elif target >= me:  # target > me
                    lo = mid + 1

            # not found
            return -1

        ### MAIN
        interval = [-1, -1]
        if len(nums) > 0:
            # TODO: populate the interval
            interval[0] = _search_start(target)  # TODO
            interval[1] = _search_ending(target)  # TODO

        return interval
