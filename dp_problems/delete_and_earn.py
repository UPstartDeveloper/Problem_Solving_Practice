from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        LeetCode: https://leetcode.com/problems/delete-and-earn/
        
        Input:
            int[len > 0, pos, dupes, unsorted]
            
            NOT Insight
                - deleting highest #'s
                
            order of deletions matters
            ASSUME multiple "correct"
            
        Intuition:
            DP
            max heap
            
        EC:
            wrong input ---> ValueError
            
        Stepping Stone:
        
            1) _delete_one_int(index)
                for loop
                "delete" ---> -1
                
            2) _get_all_unqiue(nums)                
                1 dict --> (unique val --> [indices])
                {
                    2: [0, 1],
                    3: [2, 3, 4],
                    4: [5]
                }
                
            2) _order_deletions(unique_values = [2, 3, 4])
                heuristic:
                    best order = 
                
        
        Brute Force:
            1) try out all possible del_orders
                _get_all_unqiue(nums)  # O(n)
                _order_deletions(unique_values = [2, 3, 4])
                    O(n!*n^2)
            2) store all scores we get
            3) return max(scores)
            
        Backtracking:
            Find all unique nums
            Backtrack
                - find a perm of all the unique
                - once found, compute score
                - see if the score is the max
            
        
        
        """
        ### HELPER
        def _input_invalid(nums):
            size = 0
            for num in nums:
                if isinstance(num, int) is False or num <= 0:
                    return True
                size += 1
            return size == 0
        
        ### MAIN
        # EC: invalid input
        if _input_invalid(nums):
            raise ValueError(
                f"Check that {nums} contains >= ints > 0"
            )
        # A: compute # points gain'd from taking 1 element type
        points = defaultdict(int)
        for num in nums:
            points[num] = points.get(num, 0) + num
        # B: Base cases - # if 0/1 not in dict, get 0
        two_back, one_back = points[0], points[1]
        # C: find answer
        for num in range(2, max(nums) + 1):
            # we end w/ greatest elem type; so forget about elem+1
            all_points_between_0_and_num = max(
                one_back, two_back + points.get(num, 0)
            )  
            # move on to the next subproblem
            two_back, one_back = (
                one_back, all_points_between_0_and_num
            )
        # D: all done!
        return one_back
