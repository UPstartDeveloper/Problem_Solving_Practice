from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        LeetCode: https://leetcode.com/problems/majority-element/
        
        Input/Problem:
            int[notEmpty, mutable, pos/neg, unsorted, dupes]
            ASSUME only 1 majorit 
        
        Output:
            elem --> count > n/2
            
        Intuition:
            arrays
            sorting, hashmap, pointers
            
        EC:
            - []
            - no majority
            - array too big
            
        Approach:
            
            1. histogram --> iter the histogram
                O(n) t & s
                
            2. 
                
        
        """
        ### HELPERS
        def _find_majority_using_dict(nums):
            """O(n) time + space"""
            histogram = Counter(nums)
            for num, count in histogram.items():
                if count > (len(nums) / 2):
                    return num
            return None

        def _find_majority_using_iter(nums):
            """O(n^2) time, O(1) space"""
            threshold, index = len(nums) / 2, 0
            while index < len(nums):
                elem = nums[index]
                count = 1
                last_seen_index = index
                for other_ndx in range(index + 1, len(nums)):
                    # update count
                    if nums[other_ndx] == elem:
                        count += 1
                        # swap
                        if (
                            last_seen_index < len(nums) - 1
                            and nums[last_seen_index + 1] != elem
                        ):
                            nums[other_ndx], nums[last_seen_index + 1] = (
                                nums[last_seen_index + 1],
                                nums[other_ndx],
                            )
                            last_seen_index += 1

                        # early exit
                        if count > threshold:
                            break
                # early exit
                if count > threshold:
                    return elem
                # move index fwd
                else:
                    index = last_seen_index + 1

        def _find_majority_using_suffix(nums):
            """O(n) time, O(1) space"""
            count = 0
            candidate = None
            # find the candidate (who can stay the longest)
            for num in nums:
                if count == 0:
                    candidate = num
                count += 1 if num == candidate else -1
            # all done!
            return candidate

        ### MAIN
        # 1: Histogram
        # return _find_majority_using_dict(nums)
        # 2: nested for loops
        # return _find_majority_using_iter(nums)
        # 3: use Boyer-Moore Voting Algo
        return _find_majority_using_suffix(nums)
